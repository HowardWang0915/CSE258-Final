import os
import math
import json
import gzip
import random
import argparse
import numpy as np
import dateutil.parser

from tqdm import tqdm
from sklearn import linear_model
from collections import defaultdict
from helpers.load import loadFromPickle, load_embeddings
from sklearn.metrics import mean_squared_error

parser = argparse.ArgumentParser()
parser.add_argument('--data-path', help='Path to dataset (must be pickle)', required=True)
parser.add_argument('--embed-path', help='Path to embeddings (must be npy)', required=True)
parser.add_argument('-m', '--embed-mode', help='Embedding mode (bert or w2v)', choices=['bert', 'w2v'] , required=True)
args = parser.parse_args()

if args.embed_mode == 'bert':
    print('Start loading BERT embeddings...')
    bert_train_embeddings = load_embeddings(args.embed_path)
    bert_test_embeddings = load_embeddings(args.embed_path, False)
    print('Finished loading BERT embeddings.\n')
elif args.embed_mode == 'w2v':
    # TODO: Add load Word2Vec embeddings
    pass


def features(i, d, load_ratings=False, load_embeddings=False, train=True):
    features = [1]

    if load_ratings:
        features.extend([d['review/taste'], d['review/aroma'], d['review/palate'], 
                         d['review/appearance'], len(d['review/text'])])

    if load_embeddings:
        if args.embed_mode == 'bert':
            features.extend(bert_embed_feat(i, train))
        else:
            pass # TODO: Add Word2Vec embedding func

    return features

def bert_embed_feat(i, train):
    if train:
        return bert_train_embeddings[i, :]
    else:
        return bert_test_embeddings[i, :]

def w2v_embed_feat():
    pass

def baseline(dataTrain, dataTest):
    print('Starting baseline experiment...')
    print('=========================================')

    print('Start processing data...')
    x_train, y_train, x_test, y_test = [], [], [], []

    for i, d in enumerate(dataTrain):
        x_train.append(features(i, d, True))
        y_train.append(d['review/overall'])

    for i, d in enumerate(dataTest):
        x_test.append(features(i, d, True))
        y_test.append(d['review/overall'])

    x_train, y_train, x_test, y_test = np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

    # Normalization len(review_text)
    x_test[:, 5] /= x_train[:, 5].max()
    x_train[:, 5] /= x_train[:, 5].max()

    print('Data processing finished.')

    print('Start fitting regressor...')
    regressor = linear_model.LinearRegression()
    regressor.fit(x_train, y_train)
    print('Regressor fitted.\n')

    predictions = regressor.predict(x_test)
    print('Baseline experiment finished.')
    print('Testing results (MSE) of baseline model:', mean_squared_error(y_test, predictions))
    print('Ground Truth:', y_test)
    print('Predictions:', predictions)
    print('=========================================\n')

def best_feature(dataTrain, dataTest):
    print('Starting best feature experiment...')
    print('=========================================')

    print('Start processing data...')
    x_train, y_train, x_test, y_test = [], [], [], []

    for i, d in enumerate(dataTrain):
        x_train.append(features(i, d, True))
        y_train.append(d['review/overall'])

    for i, d in enumerate(dataTest):
        x_test.append(features(i, d, True))
        y_test.append(d['review/overall'])

    x_train, y_train, x_test, y_test = np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

    # Keep best feature
    x_train = x_train[:, 2].reshape(-1, 1)
    x_test = x_test[:, 2].reshape(-1, 1)

    print('Data processing finished.')

    print('Start fitting regressor...')
    regressor = linear_model.LinearRegression()
    regressor.fit(x_train, y_train)
    print('Regressor fitted.\n')

    predictions = regressor.predict(x_test)
    print('Best feature experiment finished.')
    print('Testing results (MSE) of best feature model:', mean_squared_error(y_test, predictions))
    print('Ground Truth:', y_test)
    print('Predictions:', predictions)
    print('=========================================\n')

def bert_embedding(dataTrain, dataTest):
    print('Starting BERT embedding experiment...')
    print('=========================================')

    print('Start processing data...')
    x_train, y_train, x_test, y_test = [], [], [], []

    for i, d in enumerate(tqdm(dataTrain)):
        x_train.append(features(i, d, False, True))
        y_train.append(d['review/overall'])

    for i, d in enumerate(tqdm(dataTest)):
        x_test.append(features(i, d, False, True, False))
        y_test.append(d['review/overall'])

    x_train, y_train, x_test, y_test = np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

    print('Data processing finished.')

    print('Start fitting regressor...')
    regressor = linear_model.LinearRegression()
    regressor.fit(x_train, y_train)
    print('Regressor fitted.\n')

    predictions = regressor.predict(x_test)
    print('BERT embedding experiment finished.')
    print('Testing results (MSE) of bert embedding model:', mean_squared_error(y_test, predictions))
    print('Ground Truth:', y_test)
    print('Predictions:', predictions)
    print('=========================================\n')

def bert_with_ratings(dataTrain, dataTest):
    print('Starting BERT with rating experiment...')
    print('=========================================')

    print('Start processing data...')
    x_train, y_train, x_test, y_test = [], [], [], []

    for i, d in enumerate(tqdm(dataTrain)):
        x_train.append(features(i, d, True, True))
        y_train.append(d['review/overall'])

    for i, d in enumerate(tqdm(dataTest)):
        x_test.append(features(i, d, True, True, False))
        y_test.append(d['review/overall'])

    x_train, y_train, x_test, y_test = np.array(x_train), np.array(y_train), np.array(x_test), np.array(y_test)

    print('Data processing finished.')

    print('Start fitting regressor...')
    regressor = linear_model.LinearRegression()
    regressor.fit(x_train, y_train)
    print('Regressor fitted.\n')

    predictions = regressor.predict(x_test)
    print('BERT with rating experiment finished.')
    print('Testing results (MSE) of bert with rating model:', mean_squared_error(y_test, predictions))
    print('Ground Truth:', y_test)
    print('Predictions:', predictions)
    print('=========================================\n')



if __name__ == "__main__":
    dataset = loadFromPickle(args.data_path)
    dataTrain, dataTest = dataset[:int(len(dataset) * 0.9)], dataset[int(len(dataset) * 0.9):]

    # Baseline
    baseline(dataTrain, dataTest)

    # Best feature
    best_feature(dataTrain, dataTest)

    # BERT embedding
    bert_embedding(dataTrain, dataTest)

    # BERT with ratings
    bert_with_ratings(dataTrain, dataTest)

