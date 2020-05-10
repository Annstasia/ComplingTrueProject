import json
with open("fileJson1.json", "r") as read_file:
    newData = json.load(read_file)
print('<nodes count="{}">'.format(len(newData)))
nameList = list(newData.keys())
for i in range(len(nameList)):
    print('<node id="{}" label="{}"/>'.format(i, nameList[i]))
print(newData)
weight = 100
k = 50
x = 0
for i in range(len(nameList)):
    for j in newData[nameList[i]]["names"]:
        print('<edge id="{}" source="{}" target="{}" weight="{}"/>'.format(k, i, nameList.index(j), len(newData[nameList[i]]["names"][j][1]) * weight))
        k += 1
        # for q in range(len(newData[nameList[i]]["names"][j][1])):
print(k - 50 + 1)
