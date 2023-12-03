import statistics
import numpy as np
from helpers.load import loadFromPickle
import matplotlib.pyplot as plt
from collections import defaultdict

data = loadFromPickle('data/data.pkl')

appear = []
aroma = []
palate = []
taste = []
overall = []
beers = defaultdict(int)
beerNames = defaultdict()
reviewers = defaultdict(int)
brewers = defaultdict(int)

for d in data:
    if d['beer/beerId'] in beerNames.keys():
        if beerNames[d['beer/beerId']] != d['beer/name']:
            print("Somethings wrong!")
    beerNames[d['beer/beerId']] = d['beer/name']
    beers[d['beer/beerId']] += 1
    reviewers[d['review/profileName']] += 1
    brewers[d['beer/brewerId']] += 1
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
print("Number of unique brewers: ", len(brewers))
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

topReviewers = sorted(reviewers.items(), key=lambda x:x[1], reverse=True)[:10]
topReviewedBeers = sorted(beers.items(), key=lambda x:x[1], reverse=True)[:10]
print("List of top 10 reviewers with average rating: ")
for i in range(10):
    arr = [d['review/overall'] for d in data if d['review/profileName'] == topReviewers[i][0]]
    print(" " + topReviewers[i][0] + ":", + topReviewers[i][1], ",", sum(arr) / len(arr))
print("List of top 10 reviewed Beers with average rating: ")
for i in range(10):
    arr = [d['review/overall'] for d in data if d['beer/beerId'] == topReviewedBeers[i][0]]
    print(" " + beerNames[topReviewedBeers[i][0]] + ":", + topReviewedBeers[i][1], ",", sum(arr) / len(arr))
