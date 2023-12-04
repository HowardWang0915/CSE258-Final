import math
import statistics
import numpy as np
from helpers.load import loadFromPickle
import matplotlib.pyplot as plt
from collections import defaultdict
import pandas as pd
import seaborn as sns
import scipy

data = loadFromPickle('data/data.pkl')

appear = []
aroma = []
palate = []
taste = []
overall = []
popularity = [] # wine popularity
activity = [] # user activity
abv = []
beers = defaultdict(int)
beerNames = defaultdict()
reviewers = defaultdict(int)
brewers = defaultdict(int)
reviewerRatings = defaultdict(int)
beerRatings = defaultdict(int)
beerStyles = defaultdict(int)

for d in data:
    if d['beer/beerId'] in beerNames.keys():
        if beerNames[d['beer/beerId']] != d['beer/name']:
            assert False
    beerNames[d['beer/beerId']] = d['beer/name']
    beers[d['beer/beerId']] += 1
    reviewers[d['review/profileName']] += 1
    brewers[d['beer/brewerId']] += 1
    reviewerRatings[d['review/profileName']] += d['review/overall']
    beerRatings[d['beer/beerId']] += d['review/overall']
    beerStyles[d['beer/style']] += 1
    appear.append(d['review/appearance'])
    aroma.append(d['review/aroma'])
    palate.append(d['review/palate'])
    taste.append(d['review/taste'])
    overall.append(d['review/overall'])
    abv.append(d['beer/ABV'])
# calculate popularity 
maxPopularity = max(beers.values())
maxActivities = max(reviewers.values())
for d in data:
    popularity.append(beers[d['beer/beerId']] / maxPopularity)
    activity.append(reviewers[d['review/profileName']] / maxActivities)
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
plt.figure(6)
plt.hist(np.array(popularity),bins=20)
plt.savefig('./assets/hist_popularity.jpg')
plt.figure(7)
plt.hist(np.array(activity),bins=20)
plt.savefig('./assets/hist_activity.jpg')
plt.figure(8)
plt.hist(np.array(abv), bins=20)
plt.savefig('./assets/hist_abv.jpg')

# print(data[:3])
print("Number of unique beer IDs: ", len(beers))
print("Number of unique reviewers: ", len(reviewers))
print("Number of unique brewers: ", len(brewers))
print("Number of unique beer styles", len(beerStyles))
print("")

print("ABV: ")
print(" Average: ", statistics.fmean(abv))
print(" Min: ", min(abv))
print(" Max: ", max(abv))
print(" Median: ", statistics.median(abv))
print(" Standard Deviation: ", statistics.stdev(abv))

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
topReviewedStyles = sorted(beerStyles.items(), key=lambda x:x[1], reverse=True)
print("List of top 10 reviewers with average rating and stdev: ")
for i in range(10):
    arr = [d['review/overall'] for d in data if d['review/profileName'] == topReviewers[i][0]]
    print(" " + topReviewers[i][0] + ":", + topReviewers[i][1], ",", sum(arr) / len(arr), ",", statistics.stdev(arr))
print("")
print("List of top 10 most reviewed Beers with average rating and stdev: ")
for i in range(10):
    arr = [d['review/overall'] for d in data if d['beer/beerId'] == topReviewedBeers[i][0]]
    print(" " + beerNames[topReviewedBeers[i][0]] + ":", + topReviewedBeers[i][1], ",", sum(arr) / len(arr), ",", statistics.stdev(arr))
print("")
print("List of top reviewed styles beers with average rating and stdev: ")
for i in range(10):
    arr = [d['review/overall'] for d in data if d['beer/style'] == topReviewedStyles[i][0]]
    print(" " + topReviewedStyles[i][0] + ":", + topReviewedStyles[i][1], ",", sum(arr) / len(arr), ",", statistics.stdev(arr))
# print("")
# print("List of top 20 beers with highest ratings: ")
# topRatedBeers = sorted({n: beerRatings[n] / beers[n] for n in beers.keys()}.items(), key=lambda x:x[1], reverse=True)
# for i in range(20):
#     print(" ", beerNames[topRatedBeers[i][0]], ":", topRatedBeers[i][1], ", Amount of reviews: ", beers[topRatedBeers[i][0]])
# print("List of top 20 reviewers with highest averages ratings: ")
# highScoreReviewers = sorted({n: reviewerRatings[n] / reviewers[n] for n in reviewers.keys()}.items(), key=lambda x:x[1], reverse=True)
# for i in range(20):
#     print(" ", highScoreReviewers[i][0], ":", highScoreReviewers[i][1], ", Amount of reviews: ", reviewers[highScoreReviewers[i][0]])
# print("List of top 20 beers with lowest ratings: ")
# lowestRatedBeers = topRatedBeers[::-1]
# for i in range(20):
#     print(" ", beerNames[lowestRatedBeers[i][0]], ":", lowestRatedBeers[i][1], ", Amount of reviews: ", beers[lowestRatedBeers[i][0]])
# print("List of top 20 reviewers with lowest averages ratings: ")
# lowScoreReviewers = highScoreReviewers[::-1]
# for i in range(20):
#     print(" ", lowScoreReviewers[i][0], ":", lowScoreReviewers[i][1], ", Amount of reviews: ", reviewers[lowScoreReviewers[i][0]])
# meanPop = statistics.mean(popularity)
# stdPop = statistics.stdev(popularity)
# pop = [(i - meanPop) / stdPop for i in popularity]
# print(statistics.mean(pop))
# print(statistics.stdev(pop))
# print(max(pop))
# print(min(pop))
print("Plotting feature relation pairplot")
d1 = {'abv': abv, 'appear': appear, 'aroma': aroma, 'palate': palate, 'taste': taste, 'overall': overall}
d2 = {'popularity': [math.log(i, 20) for i in popularity], 'activity': [math.log(i, 20) for i in activity], 'overall': overall}
df1 = pd.DataFrame(d1)
fig = sns.PairGrid(df1)
def pairgrid_heatmap(x, y, **kws):
    cmap = sns.light_palette(kws.pop("color"), as_cmap=True)
    plt.hist2d(x, y, cmap=cmap, cmin=1, **kws)
fig.map_diag(plt.hist)
fig.map_offdiag(pairgrid_heatmap)

plt.savefig("assets/pairplot1.jpg")
plt.close()
df2 = pd.DataFrame(d2)
fig = sns.PairGrid(df2)
fig.map_diag(plt.hist)
fig.map_offdiag(pairgrid_heatmap)
plt.savefig("assets/pairplot2.jpg")

print(" ")
print("Pearson similarity coefficient between overall and activity is", scipy.stats.pearsonr(df2['overall'], df2['activity'])[0])
print("Pearson similarity coefficient between overall and popularity is", scipy.stats.pearsonr(df2['overall'], df2['popularity'])[0])
print("Pearson similarity coefficient between activity and popularity is", scipy.stats.pearsonr(df2['activity'], df2['popularity'])[0])
print("Pearson similarity coefficient between overall and taste is", scipy.stats.pearsonr(df1['overall'], df1['taste'])[0])
print("Pearson similarity coefficient between overall and aroma is", scipy.stats.pearsonr(df1['overall'], df1['aroma'])[0])
print("Pearson similarity coefficient between overall and appearance is", scipy.stats.pearsonr(df1['overall'], df1['appear'])[0])
