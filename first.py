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


namesDict = {
    "алёша": "алеша",
    "алеш": "алеша",
    "алешка": "алеша",

    "иванов": "иван",
    "ивановна": "иван",
    "владимер": "владимир",
    "маринка": "маринка",
    "марин": "маринка",
    "марина": "маринка",

    "добрынюшка": "добрыня",
    "туграетин": "тугарин",
    "святогорския": "святогор",

    "муромля": None,
    "млада": None,
    "раставимша": None,
    "ножишшо": None,
    "умывалася": None,







}

MiddleDict={
    "никитиевич": "никитич",
    "олександровна": "александровна"
}

LastDictionary={

    "хлеб": None,
    "в": None,
    "тугаретин": "тугарин",
    "микула": "микула",
    "с": None,
    "скоро": None,
    "своё": None,
    "наливавшая": None,
    "ивановичь": "иванович",
    "третий": None,
    "та": None,
    "а": None,
    "середняго": None,
    "заперлася": None,
    "из": None,
    "возмеш"
    "терема": None,
    "приставай": None,
    "приезжай": None,
    "водилася": None,
    "здымалеькая": None,
    "бела": None,
    "обвернулася": None,
    "умывалася": None,
    "з": None,
    "к": None,
    "и": None,
    "хорошая": None,
    "молодая": None,
    "белых": None


}

LastShouldStrange={
    "князь": "князь"
}
LastShouldFirst = {
    "микула": "микула",
    "добрынин": "добрыня",
    "микулов": "микула",
    "маринин": "марина",
    "алешенек": "алеша",
    "еким": "еким",
    "ильюшенка": "илья"



}

morph = pymorphy2.MorphAnalyzer()

extractor = NamesExtractor()

path = 'bil/'
fnames = os.listdir(path)
arr = {}
was_names = []
spans = []
borders = 200


nothing1 = set()
nothing2 = set()
nothing3 = set()



# Потом поменяю выбор файлов. Так пока удобнее
for name in range(20):
    spans = []
    # по очереди открываем файлы и извлекаем имена
    with open(path + str(name) + "/" + str(name) + ".txt", 'r', encoding='utf-8') as f:
        text = f.read().strip()
    matches = extractor(text)

    for match in matches:
        # spans.append(match.span) # Запоминаю позицию имени, чтобы потом рассмотреть слова поблизости и охарактеризовать героя
        # обрабатываем извлеченные имена



        spans.append(match.span)  # Запоминаю позицию имени, чтобы потом рассмотреть слова поблизости и охарактеризовать героя
        #
        was_names.append(str(match.fact.first) + " " + str(match.fact.middle) + " " + str(match.fact.last))

        # if (match.fact.first !=None):
        # #
        #     nothing1.add(match.fact.first if match.fact.first not in namesDict else namesDict[match.fact.first])
        # if (match.fact.middle !=None):
        #     nothing2.add(match.fact.middle if match.fact.middle not in MiddleDict else MiddleDict[match.fact.middle])
        # if (match.fact.last !=None):
        #     nothing3.add(match.fact.last if match.fact.last not in LastDictionary else LastDictionary[match.fact.last])


        # if (match.fact.first != None and match.fact.last != None and match.fact.middle):
        #     was_names.append(match.fact.first + " " + match.fact.middle + match.fact.last)
        # elif match.fact.first != None and match.fact.last != None:
        #     was_names.append(match.fact.first + " None" + match.fact.last)
        # elif (match.fact.first != None and match.fact.middle != None):
        #     was_names.append(match.fact.first + " " + match.fact.middle)
        # elif (match.fact.last != None and match.fact.middle != None):
        #     was_names.append(match.fact.middle + " " + match.fact.last)
        # elif (match.fact.middle != None):
        #     was_names.append(match.fact.middle)
        # elif match.fact.first != None:
        #     was_names.append(match.fact.first)
        # # elif match.fact.last != None:
        # #     was_names.append(match.fact.last)
    # ------------------------------------------------------------------------------------------------------------------
    for i in range(len(was_names)):
        # Запись имен в словарь. Каждому персонажу присваивается множество персонажей, с которыми он встретился в одном тексте
        if not(was_names[i] in arr):
            arr[was_names[i]] = {"names": {}, "characteristic": [], "count": 0, "text_number":[]}

        arr[was_names[i]]["count"] += 1
        if (name not in arr[was_names[i]]["text_number"]):
            arr[was_names[i]]["text_number"].append(name)
        for j in range(len(was_names)):
            if (j == i):
                continue
            # if (not was_names[j] in arr[was_names[i]]["names"]):
            if (was_names[j] not in arr[was_names[i]]["names"]):
                arr[was_names[i]]["names"][was_names[j]] = [0, []]
            arr[was_names[i]]["names"][was_names[j]][0] += 1
            if name not in arr[was_names[i]]["names"][was_names[j]][1]:
                arr[was_names[i]]["names"][was_names[j]][1].append(name)
        # for j in range(i+1, len(was_names)):
        #     arr[was_names[i]]["names"].add(was_names[j])
    #
    text = text.lower()
    for _ in range(len(spans)):
        i = spans[_]
        # Выбор поддтекста. Из этой части будет извлекаться характеристика персонажей
        borderLeft = max(0, i[0] - 200)
        while text[borderLeft] != ' ':
            borderLeft+=1
        borderRight = min(i[1] + 200, len(text) - 1)
        while text[borderRight] != ' ':
            borderRight -= 1
        # subText = word_tokenize(text[borderLeft + 1:borderRight])
        # subText = [i for i in subText if (i not in string.punctuation)]
        # stop_words = stopwords.words('russian')
        # stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'во', 'уж', '—', 'к', 'на', 'ко'])
        # subText = [i for i in subText if (i not in stop_words)]
        # characteristic = []
        # for j in subText:
        #     p = morph.parse(j)
        #     pos = p[0].tag.POS
        #     # Характеристика строится на основе прилагательных
        #     if (pos == "ADJF" or pos == "ADJS"):
        #         characteristic.append(j)
        arr[was_names[_]]["characteristic"].append(text[borderLeft + 1:borderRight])
    # -------------------------------------------------------------------------------------------------------------------
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
