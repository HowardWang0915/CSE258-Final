import gzip

with gzip.open("data/ratebeer.json.gz", mode='rt') as f:
    data = f.read()

