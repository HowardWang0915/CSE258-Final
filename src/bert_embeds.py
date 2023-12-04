import os
import gzip
import json
import torch
import argparse
import numpy as np

from tqdm import tqdm
from helpers.load import loadFromPickle
from helpers.cleanData import cleanData
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from transformers import AutoModel, AutoTokenizer


MODEL_NAME = 'bert-base-uncased'
BATCH_SIZE = 64

if torch.backends.mps.is_available():
    device = torch.device('mps')
    print('Using MPS as torch device.')
else:
    device = torch.device('cpu')
    print('MPS is not available.')


def get_embeddings(text, tokenizer, model):
    tokens = tokenizer(text, return_tensors='pt', padding=True, truncation=True).to(device)
    
    with torch.no_grad():
        output = model(**tokens)

    embeddings = output.last_hidden_state.mean(dim=1)
    return embeddings

def save_tensor(data, filename):
    # data = torch.tensor(data)
    # torch.save(data, filename)
    np.save(filename, data)
    print(f'{filename} saved.')

def train(tokenizer, model, data_path):
    # dataset = parse()
    dataset = loadFromPickle(data_path)

    # dataTrain: 9000
    # dataTest: 1000
    dataTrain, dataTest = dataset[:int(len(dataset)*0.9)], dataset[int(len(dataset)*0.9):]
    print(f'Training size: {len(dataTrain)}, testing size {len(dataTest)}')

    x_train, y_train, x_test, y_test = [], [], [], []

    print('Start processing data...')

    # Process train data
    # The training data will be the embedding of the review text
    # x -> [embedding(d['review/text'])]
    for i in tqdm(range(0, len(dataTrain), BATCH_SIZE)):
        reviews = [d['review/text'] for d in dataTrain[i:i+BATCH_SIZE]]
        ratings = [d['review/overall'] for d in dataTrain[i:i+BATCH_SIZE]]
        embeddings = get_embeddings(reviews, tokenizer, model)

        if device != torch.device('cpu'):
            x_train.extend(embeddings.cpu().detach().numpy().tolist())
        else:
            x_train.extend(embeddings.tolist())

        y_train.extend(ratings)
    
    for i in tqdm(range(0, len(dataTest), BATCH_SIZE)):
        reviews = [d['review/text'] for d in dataTest[i:i+BATCH_SIZE]]
        ratings = [d['review/overall'] for d in dataTest[i:i+BATCH_SIZE]]
        embeddings = get_embeddings(reviews, tokenizer, model)

        if device != torch.device('cpu'):
            x_test.extend(embeddings.cpu().detach().numpy().tolist())
        else:
            x_test.extend(embeddings.tolist())

        y_test.extend(ratings)

    x_train, y_train, x_test, y_test = np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

    print('Start saving embeddings...')
    # Save tensor
    save_tensor(x_train, 'embeddings/train.npy')
    save_tensor(x_test, 'embeddings/test.npy')

    print('Finished processing data, start training regressor...')

    regressor = LinearRegression()
    regressor.fit(x_train, y_train)
    print('Regressor trained.')

    print('Start testing...')
    predicts = regressor.predict(x_test)
    print('Testing results:', mean_squared_error(y_test, predicts))

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModel.from_pretrained(MODEL_NAME)
    model.to(device)

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Data path', required=True)
    args = parser.parse_args()

    train(tokenizer, model, args.path)

