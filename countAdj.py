import json
import pprint
from collections import Counter

with open("newNewData1.json.json") as f:
    adjects = json.load(f)
newData = {}
for i in adjects:
    newData[i] = Counter(adjects[i])
pprint.pprint(newData)