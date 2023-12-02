import statistics
from helpers.load import loadFromPickle
from helpers.cleanData import cleanData

data = loadFromPickle()

beers = set()
reviewers = set()

data = cleanData(data)
for d in data:
    beers.add(d['beer/beerId'])
    reviewers.add(d['review/profileName'])
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

