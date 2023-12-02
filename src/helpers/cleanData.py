import re
def cleanData(data):
    for d in data:
        d['beer/ABV'] = float(d['beer/ABV']) if d['beer/ABV'].replace(".", "").isdigit() else 0
        d['review/appearance'] = [float(s) for s in re.findall(r'-?\d+\.?\d*', d['review/appearance'])][0]
        d['review/aroma'] = [float(s) for s in re.findall(r'-?\d+\.?\d*', d['review/aroma'])][0]
        d['review/palate'] = [float(s) for s in re.findall(r'-?\d+\.?\d*', d['review/palate'])][0]
        d['review/taste'] = [float(s) for s in re.findall(r'-?\d+\.?\d*', d['review/taste'])][0]
        d['review/overall'] = [float(s) for s in re.findall(r'-?\d+\.?\d*', d['review/overall'])][0]
    return data
