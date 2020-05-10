import json
from asyncore import file_dispatcher

from natasha import NamesExtractor
import nltk
import os
path = 'bil/'
with open("fileJson2.json", "r") as read_file:
    names = json.load(read_file)
extractor = NamesExtractor()

def findX(name):
    print(name, end="! ")
    lessImportant = []
    moreImportant = []

    for i in names:
        if (name.startswith(i)):
            moreImportant.append(names[i])
        elif (i in name):
            lessImportant.append(names[i])
            # print(names[i], end=" ")

    if (len(moreImportant) != 0):
        print(*moreImportant)
    else:
        print(*lessImportant)
    print()

for name in range(20):
    spans = []
    # по очереди открываем файлы и извлекаем имена
    with open(path + str(name) + "/" + str(name) + ".txt", 'r', encoding='utf-8') as f:
        text = f.read().strip()
    matches = extractor(text)

    for match in matches:
        first = ""
        second = ""
        last = ""
        if (match.fact.first) != None:
            first = match.fact.first + " "
        if (match.fact.middle) != None:
            second = match.fact.middle + " "
        if (match.fact.last) != None:
            last = match.fact.last

        findX(first + second + last)
