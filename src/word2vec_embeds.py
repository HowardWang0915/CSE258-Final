from helpers.load import loadFromPickle
from gensim.models import Word2Vec
import argparse
import string
import numpy as np

def sentence_embedding(sentence, model):
    if(len(sentence) == 0): return np.zeros(model.vector_size)
    word_embeddings = [model.wv[word] if word in model.wv else np.zeros(model.vector_size) for word in sentence]
    return np.mean(word_embeddings, axis=0)

def train(dataPath, vs=200, win=3):
    dataset = loadFromPickle(dataPath)
    reviews = [d['review/text'] for d in dataset]
    print('Tokenizing...')
    reviewTokens = []
    punctuation = set(string.punctuation)
    for r in reviews:
        r = ''.join([c for c in r.lower() if not c in punctuation])
        tokens = []
        for w in r.split():
            tokens.append(w)
        reviewTokens.append(tokens)
    trainReviewTokens, testReviewTokens = reviewTokens[:int(len(dataset)*0.9)], reviewTokens[int(len(dataset)*0.9):]
    print('Word2Vec Training...')
    model = Word2Vec(sentences=trainReviewTokens,
                     min_count=5, # Words/items with fewer instances are discarded
                     vector_size=vs, # Model dimensionality
                     window=win, # Window size
                     sg=1) # Skip-gram model
    print('Saving embeddings...')
    trainEmbedding = np.array([sentence_embedding(sentence, model) for sentence in trainReviewTokens])
    np.save('../embeddings/Word2Vec/train.npy', trainEmbedding)
    testEmbedding = np.array([sentence_embedding(sentence, model) for sentence in testReviewTokens])
    np.save('../embeddings/Word2Vec/test.npy', testEmbedding)
    print('Finish!')
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Data path', required=True)
    args = parser.parse_args()

    train(args.path)