import statistics
import numpy as np
from helpers.load import loadFromPickle
import matplotlib.pyplot as plt

data = loadFromPickle('data/data.pkl')

beers = set()
reviewers = set()
appear = []
aroma = []
palate = []
taste = []
overall = []
for d in data:
    beers.add(d['beer/beerId'])
    reviewers.add(d['review/profileName'])
    appear.append(d['review/appearance'])
    aroma.append(d['review/aroma'])
    palate.append(d['review/palate'])
    taste.append(d['review/taste'])
    overall.append(d['review/overall'])

# generate histogram of all review scores
plt.figure(1)
plt.hist(np.array(appear),bins=20)
plt.savefig('./assets/hist_appear.jpg')
plt.figure(2)
plt.hist(np.array(aroma),bins=20)
plt.savefig('./assets/hist_aroma.jpg')
plt.figure(3)
plt.hist(np.array(palate),bins=20)
plt.savefig('./assets/hist_palate.jpg')
plt.figure(4)
plt.hist(np.array(taste),bins=20)
plt.savefig('./assets/hist_taste.jpg')
plt.figure(5)
plt.hist(np.array(overall),bins=20)
plt.savefig('./assets/hist_overall.jpg')

# print(data[:3])
print("Number of unique beer IDs: ", len(beers))
print("Number of unique reviewers: ", len(reviewers))
print("Appearance: ")
print(" Average: ", statistics.fmean(appear))
print(" Min: ", min(appear))
print(" Max: ", max(appear))
print(" Median: ", statistics.median(appear))
print(" Standard Deviation: ", statistics.stdev(appear))

print("Aroma: ")
print(" Average: ", statistics.fmean(aroma))
print(" Min: ", min(aroma))
print(" Max: ", max(aroma))
print(" Median: ", statistics.median(aroma))
print(" Standard Deviation: ", statistics.stdev(aroma))

print("Palate: ")
print(" Average: ", statistics.fmean(palate))
print(" Min: ", min(palate))
print(" Max: ", max(palate))
print(" Median: ", statistics.median(palate))
print(" Standard Deviation: ", statistics.stdev(palate))

print("Taste: ")
print(" Average: ", statistics.fmean(taste))
print(" Min: ", min(taste))
print(" Max: ", max(taste))
print(" Median: ", statistics.median(taste))
print(" Standard Deviation: ", statistics.stdev(taste))

print("Overall: ")
print(" Average: ", statistics.fmean(overall))
print(" Min: ", min(overall))
print(" Max: ", max(overall))
print(" Median: ", statistics.median(overall))
print(" Standard Deviation: ", statistics.stdev(overall))

