import argparse
import gzip
import pickle
from tqdm import tqdm

def loadAndSave(count):
    """
    load the dataset and save them in pickle format for later use.
    """
    data = []
    with gzip.open("data/ratebeer.json.gz", mode='rt') as f:
        lines = f.readlines()
        for i in tqdm(range(count)):
            data.append(eval(lines[i])) 
    with open("data/data.pkl", mode='wb') as f:
        pickle.dump(data, f)

def loadFromPickle():
    """
    Load the saved pickle data for speed access
    """
    with open('data/data.pkl', mode='rb') as f:
        data = pickle.load(f)
    return data
    
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--count", help="Number of data to be loaded")
    args = parser.parse_args()
    loadAndSave(int(args.count))
