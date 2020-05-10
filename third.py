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


def appendSpans(span):
    start = span[0] - 200
    end = span[1] + 200
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
        if (name.startswith(i)):
            if (len(names[i]) != 1):
                print(text[max(start - 100, 0):min(len(text) - 1, start + 100)])
                print(names[i])
                inp = input()
                if (inp != ""):
                    moreImportant.append(inp)
            else:
                moreImportant.append(names[i][0])
        elif (i in name):
            if (len(names[i]) != 1):
                print(text[max(start - 100, 0):min(len(text) - 1, start + 100)])
                print(names[i])
                inp = input()
                if (inp != ""):
                    lessImportant.append(inp)
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

extractor = NamesExtractor()

path = 'bil1/'
fnames = os.listdir(path)
arr = {}
was_names = []
spans = {}
borders = 200


nothing1 = set()
nothing2 = set()
nothing3 = set()



# Потом поменяю выбор файлов. Так пока удобнее
for name in range(1, 41):
    spans = {}
    # по очереди открываем файлы и извлекаем имена
    with open(path + str(name), 'r', encoding='utf-8') as f:
        text = f.read().strip()
    matches = extractor(text)

    for match in matches:
        # spans.append(match.span) # Запоминаю позицию имени, чтобы потом рассмотреть слова поблизости и охарактеризовать героя
        # обрабатываем извлеченные имена
        # spans.append(match.span)  # Запоминаю позицию имени, чтобы потом рассмотреть слова поблизости и охарактеризовать героя
        #

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
            # print(was_names[-1] == "Илья Муромец")
            appendSpans(match.span)
            # spans[was_names[-1]].append(match.span)

    # ------------------------------------------------------------------------------------------------------------------
    for i in range(len(was_names)):
        # Запись имен в словарь. Каждому персонажу присваивается множество персонажей, с которыми он встретился в одном тексте
        if not(was_names[i] in arr):
            arr[was_names[i]] = {"names": {}, "characteristic": [], "smallCharacteristic":[], "count": 0, "text_number":[]}

        arr[was_names[i]]["count"] += 1
        if (name not in arr[was_names[i]]["text_number"]):
            arr[was_names[i]]["text_number"].append(name)
        for j in range(len(was_names)):
            if (was_names[j] == was_names[i]):
                continue
            if (was_names[j] not in arr[was_names[i]]["names"]):
                arr[was_names[i]]["names"][was_names[j]] = [0, []]
            arr[was_names[i]]["names"][was_names[j]][0] += 1
            if name not in arr[was_names[i]]["names"][was_names[j]][1]:
                arr[was_names[i]]["names"][was_names[j]][1].append(name)
    #
    text = text.lower()
    for name in set(was_names):
        for i in range(len(spans[name]["Start"])):
            borderLeft = max(0, spans[name]["Start"][i])
            # while text[borderLeft] != ' ' and borderLeft < len(text) - 2:
            #     borderLeft += 1
            borderRight = min(spans[name]["End"][i], len(text) - 1)
            # while text[borderRight] != ' ' and borderRight > 0:
            #     borderRight -= 1
            arr[name]["characteristic"].append(text[borderLeft + 1:borderRight])
            change = (borderRight - borderLeft) // 3
            arr[name]["smallCharacteristic"].append(text[borderLeft + 1 + change:borderRight - change])

        # Выбор поддтекста. Из этой части будет извлекаться характеристика персонажей
    #     borderLeft = max(0, i[0] - 200)
    #     while text[borderLeft] != ' ' and borderLeft < len(text) - 2:
    #         borderLeft+=1
    #     borderRight = min(i[1] + 200, len(text) - 1)
    #     while text[borderRight] != ' ' and borderRight > 0:
    #         borderRight -= 1
    #     # subText = word_tokenize(text[borderLeft + 1:borderRight])
    #     # subText = [i for i in subText if (i not in string.punctuation)]
    #     # stop_words = stopwords.words('russian')
    #     # stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'во', 'уж', '—', 'к', 'на', 'ко'])
    #     # subText = [i for i in subText if (i not in stop_words)]
    #     # characteristic = []
    #     # for j in subText:
    #     #     p = morph.parse(j)
    #     #     pos = p[0].tag.POS
    #     #     # Характеристика строится на основе прилагательных
    #     #     if (pos == "ADJF" or pos == "ADJS"):
    #     #         characteristic.append(j)
    #     # print(arr[was_names[_]]["characteristic"])
    #     arr[was_names[_]]["characteristic"].append(text[borderLeft + 1:borderRight])
    # # -------------------------------------------------------------------------------------------------------------------
    was_names = []


# jsonDict = json.dumps(arr)
print(arr)
with open("fileJson1.json", "w", encoding="utf-8") as file:
    json.dump(arr, file, ensure_ascii=False)
print("ok ")

# print(nothing1)
# print(nothing2)
# print(nothing3)
# #
# # pprint(arr)
# for i in arr:
#     print(i)
#     for j in arr[i]["names"]:
#         print("\t", j)
#
#
#
