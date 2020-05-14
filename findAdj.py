# import json
# import pprint
# import string
#
# import nltk
# import pymorphy2
# from nltk.corpus import stopwords
#
# with open("fileJson1.json", "r") as read_file:
#     newData = json.load(read_file)
# newNewData={}
# for i in newData:
#     newNewData[i] = []
#
#     for text in newData[i]["smallCharacteristic"]:
#         for j in string.punctuation:
#             text = text.replace(j, " ")
#         words = nltk.word_tokenize(text)
#         delta = len(words) // 3
#         words = words[delta:len(words)-delta]
#         morph = pymorphy2.MorphAnalyzer()
#         words1 = []
#         q = 0
#
#         stop_words = set(stopwords.words("russian"))
#
#         for j in words:
#             parsed = morph.parse(j)[0]
#             lemma = parsed.normal_form
#             if (parsed.tag.POS=="ADJS" or parsed.tag.POS=="ADJF"):
#                 newNewData[i].append(lemma)
# with open("newNewData1.json", "w", encoding="utf-8") as file:
#     json.dump(newNewData, file, ensure_ascii=False)
# # print(newNewData)
# newNewNewData={}
# for i in newNewData:
#     newNewNewData[i] = nltk.Counter(newNewData[i])
# pprint.pprint(newNewNewData)

from natasha import NamesExtractor
import nltk
import os
import string
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from pprint import pprint
import pymorphy2
import json


with open("fileJson2.json", "r") as read_file:
    names = json.load(read_file)
extractor = NamesExtractor()


def appendSpans(span, delta, spans):
    start = span[0] - delta
    end = span[1] + delta
    # spans[was_names[-1]] = {"Start": [], "End": []} # убрать
    if (was_names[-1] not in spans):
        spans[was_names[-1]] = {"Start": [], "End": []}
    k = len(spans[was_names[-1]]["Start"])
    includes = False
    insertPos = -1
    key = was_names
    for i in range(k):
        if start <= spans[was_names[-1]]["Start"][i]:
            # if (end <= spans[was_names[-1]]["Start"][i]):
            #     spans[was_names[-1]]["Start"].insert(i, start)
            #     spans[was_names[-1]]["End"].insert(i, end)
            #     break
            if (spans[was_names[-1]]["Start"][i] <= end <= spans[was_names[-1]]["End"][i]):
                spans[was_names[-1]]["Start"][i] = start
                includes = True
                break
            elif (end >= spans[was_names[-1]]["End"][i]):
                spans[was_names[-1]]["Start"][i] = start
                spans[was_names[-1]]["End"][i] = end
                includes = True
                break
        elif (spans[was_names[-1]]["Start"][i] <= start <= spans[was_names[-1]]["End"][i]):
            if (spans[was_names[-1]]["Start"][i] <= end <= spans[was_names[-1]]["End"][i]):
                includes = True
            elif (end >= spans[was_names[-1]]["End"][i]):
                spans[was_names[-1]]["End"][i] = end
                includes = True
                break
        if (insertPos == -1 and spans[was_names[-1]]["Start"][i] <= start):
            insertPos = i
    if (includes==False):
        if (insertPos != -1):
            spans[was_names[-1]]["Start"].insert(insertPos, start)
            spans[was_names[-1]]["End"].insert(insertPos, end)
        else:
            spans[was_names[-1]]["Start"].append(start)
            spans[was_names[-1]]["End"].append(end)


def findX(name, start):
    name = name.replace("ё", "е")
    lessImportant = []
    moreImportant = []

    for i in names:
        if (i in name and not any([j in name for j in names[i][-1]])):
            if (name.startswith(i)):
                if (len(names[i]) != 2):
                    continue
                else:
                    moreImportant.append(names[i][0])

            else:
                if (len(names[i]) != 2):
                    continue
                else:
                    lessImportant.append(names[i][0])
            # print(names[i], end=" ")

    if (len(moreImportant) != 0):
        # print(*moreImportant)
        was_names.append(moreImportant[0])
        return True
    elif (len(lessImportant) != 0):
        # print(*lessImportant)
        was_names.append(lessImportant[0])
        return True
    return False
    # print()



morph = pymorphy2.MorphAnalyzer()
morph = pymorphy2.MorphAnalyzer()


path = 'bil1/'
fnames = os.listdir(path)
arr = {}
was_names = []
SmallSpans = {}
LargeSpans = {}
borders = 200


nothing1 = set()
nothing2 = set()
nothing3 = set()

dict1 = {}
extractor = NamesExtractor()
# Потом поменяю выбор файлов. Так пока удобнее
for name in range(1, 41):
    spans = {}
    # по очереди открываем файлы и извлекаем имена
    with open(path + str(name), 'r', encoding='utf-8') as f:
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

        if (findX(first + second + last, match.span[0])):
            if (was_names[-1] not in dict1):
                dict1[was_names[-1]] = []
            start = match.span[0]
            end = match.span[1]
            if (start != 0):
                start -= 1
            if (end != len(text) - 1):
                end+= 1
            el = ""
            while el != " " and el != "\n" and start != 0:
                start -= 1
                el = text[start]
            word = text[start:match.span[0]].strip()
            for q in string.punctuation:
                word = word.replace(q, "")
            # print(str(start) + " " + word, end=" ")
            parsed = morph.parse(word)[0]
            lemma = parsed.normal_form
            if (parsed.tag.POS == "ADJF" or parsed.tag.POS == "ADJS"):
                dict1[was_names[-1]].append(lemma)
            el = ""
            while el != " " and el != "\n" and end != len(text) - 1:
                end+=1
                el = text[end]
            for q in string.punctuation:
                word = word.replace(q, "")
            word = text[match.span[1]:end].strip()
            # print(word)
            parsed = morph.parse(word)[0]
            lemma = parsed.normal_form
            if (parsed.tag.POS == "ADJF" or parsed.tag.POS == "ADJS"):
                dict1[was_names[-1]].append(lemma)
print(dict1)
with open("newNewData1.json.json", "w", encoding="utf-8") as file:
    json.dump(dict1, file, ensure_ascii=False)
# ------------------------------------------------------------------------------------------------------------------



# jsonDict = json.dumps(arr)
# print(arr)
# with open("fileJson1.json", "w", encoding="utf-8") as file:
#     json.dump(arr, file, ensure_ascii=False)
# print("ok ")
#
