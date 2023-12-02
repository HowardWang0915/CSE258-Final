import os
import gzip
import json
import torch
import numpy as np

from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from transformers import AutoModel, AutoTokenizer


MODEL_NAME = 'bert-base-uncased'


def parse(path):
    dataset = []
    g = gzip.open(path, 'r')
    i = 0
    for l in g:
        dataset.append(eval(l))
        i += 1
        if i >= 10000:
            break

    return dataset

def get_embeddings(text, tokenizer, model):
    tokens = tokenizer(text, return_tensors='pt')
    
    with torch.no_grad():
        output = model(**tokens)

    embeddings = output.last_hidden_state.mean(dim=1)
    return embeddings

def get_rating(rating_text):
    score, total = rating_text.split('/')
    
    return float(score) / float(total)

def train(tokenizer, model):
    dataset = parse('ratebeer.json.gz')

    # dataTrain: 9000
    # dataTest: 1000
    dataTrain, dataTest = dataset[:int(len(dataset)*0.9)], dataset[int(len(dataset)*0.9):]
    print(f'Training size: {len(dataTrain)}, testing size {len(dataTest)}')

    x_train, y_train, x_test, y_test = [], [], [], []

    print('Start processing data...')

    # Process train data
    # The training data will be the embedding of the review text
    # x -> [embedding(d['review/text'])]
    for i, d in enumerate(dataTrain):
        if i % 100 == 0:
            print(f'Processing train data @{i}...')
        
        # y
        rating = get_rating(d['review/overall'])

        # x
        review = d['review/text']
        try:
            embeddings = get_embeddings(review, tokenizer, model)[0]
        except:
            print('Reivew text length exceeded at:', len(review))
            continue

        x_train.append(embeddings)
        y_train.append(rating)

    # Process test data
    for i, d in enumerate(dataTest):
        if i % 100 == 0:
            print(f'Processing train data @{i}...')
            
        rating = get_rating(d['review/overall'])
        review = d['review/text']
        try:
            embeddings = get_embeddings(review, tokenizer, model)[0]
        except:
            print('Reivew text length exceeded at:', len(review))
            continue
        
        x_test.append(embeddings)
        y_test.append(rating)

    x_train, y_train, x_test, y_test = np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

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

    train(tokenizer, model)


