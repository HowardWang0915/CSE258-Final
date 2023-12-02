import statistics
import numpy as np
from helpers.load import loadFromPickle
import matplotlib.pyplot as plt

data = loadFromPickle('data/data.pkl')

beers = set()
reviewers = set()

for d in data:
    beers.add(d['beer/beerId'])
    reviewers.add(d['review/profileName'])

# generate histogram of all review scores
plt.figure(1)
plt.hist(np.array([d['review/appearance'] for d in data]),bins=20)
plt.savefig('./assets/hist_appear.jpg')
plt.figure(2)
plt.hist(np.array([d['review/aroma'] for d in data]),bins=20)
plt.savefig('./assets/hist_aroma.jpg')
plt.figure(3)
plt.hist(np.array([d['review/palate'] for d in data]),bins=20)
plt.savefig('./assets/hist_palate.jpg')
plt.figure(4)
plt.hist(np.array([d['review/taste'] for d in data]),bins=20)
plt.savefig('./assets/hist_taste.jpg')
plt.figure(5)
plt.hist(np.array([d['review/overall'] for d in data]),bins=20)
plt.savefig('./assets/hist_overall.jpg')

# print(data[:3])
print("Number of unique beer IDs: ", len(beers))
print("Number of unique reviewers: ", len(reviewers))
print("Appearance: ")
print(" Average: ", statistics.fmean([d['review/appearance'] for d in data]))
print(" Min: ", min([d['review/appearance'] for d in data]))
print(" Max: ", max([d['review/appearance'] for d in data]))
print(" Median: ", statistics.median([d['review/appearance'] for d in data]))
print(" Standard Deviation: ", statistics.stdev([d['review/appearance'] for d in data]))

print("Aroma: ")
print(" Average: ", statistics.fmean([d['review/aroma'] for d in data]))
print(" Min: ", min([d['review/aroma'] for d in data]))
print(" Max: ", max([d['review/aroma'] for d in data]))
print(" Median: ", statistics.median([d['review/aroma'] for d in data]))
print(" Standard Deviation: ", statistics.stdev([d['review/aroma'] for d in data]))

print("Palate: ")
print(" Average: ", statistics.fmean([d['review/palate'] for d in data]))
print(" Min: ", min([d['review/palate'] for d in data]))
print(" Max: ", max([d['review/palate'] for d in data]))
print(" Median: ", statistics.median([d['review/palate'] for d in data]))
print(" Standard Deviation: ", statistics.stdev([d['review/palate'] for d in data]))

print("Taste: ")
print(" Average: ", statistics.fmean([d['review/taste'] for d in data]))
print(" Min: ", min([d['review/taste'] for d in data]))
print(" Max: ", max([d['review/taste'] for d in data]))
print(" Median: ", statistics.median([d['review/taste'] for d in data]))
print(" Standard Deviation: ", statistics.stdev([d['review/taste'] for d in data]))

print("Overall: ")
print(" Average: ", statistics.fmean([d['review/overall'] for d in data]))
print(" Min: ", min([d['review/overall'] for d in data]))
print(" Max: ", max([d['review/overall'] for d in data]))
print(" Median: ", statistics.median([d['review/overall'] for d in data]))
print(" Standard Deviation: ", statistics.stdev([d['review/overall'] for d in data]))

