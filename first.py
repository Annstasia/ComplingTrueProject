from natasha import NamesExtractor
import nltk
import os
import string
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from collections import Counter
from pprint import pprint
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

extractor = NamesExtractor()

path = 'bil/'
fnames = os.listdir(path)
arr = {}
was_names = []
spans = []
borders = 200

# Потом поменяю выбор файлов. Так пока удобнее
for name in range(20):
    spans = []
    # по очереди открываем файлы и извлекаем имена
    with open(path + str(name) + "/" + str(name) + ".txt", 'r', encoding='utf-8') as f:
        text = f.read().strip()
    matches = extractor(text)

    for match in matches:
        spans.append(match.span) # Запоминаю позицию имени, чтобы потом рассмотреть слова поблизости и охарактеризовать героя
        # обрабатываем извлеченные имена
        if (match.fact.first != None and match.fact.last != None and match.fact.middle):
            was_names.append(match.fact.first + " " + match.fact.middle + match.fact.last)
        elif match.fact.first != None and match.fact.last != None:
            was_names.append(match.fact.first + " " + match.fact.last)
        elif (match.fact.first != None and match.fact.middle != None):
            was_names.append(match.fact.first + " " + match.fact.middle)
        elif (match.fact.last != None and match.fact.middle != None):
            was_names.append(match.fact.middle + " " + match.fact.last)
        elif (match.fact.middle != None):
            was_names.append(match.fact.middle)
        elif match.fact.first != None:
            was_names.append(match.fact.first)
        elif match.fact.last != None:
            was_names.append(match.fact.last)

    for i in range(len(was_names)):
        # Запись имен в словарь. Каждому персонажу присваивается множество персонажей, с которыми он встретился в одном тексте
        if not(was_names[i] in arr):
            arr[was_names[i]] = {"names": set(), "characteristic": []}
        for j in range(i):
            arr[was_names[i]]["names"].add(was_names[j])
        for j in range(i+1, len(was_names)):
            arr[was_names[i]]["names"].add(was_names[j])

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
        subText = word_tokenize(text[borderLeft + 1:borderRight])
        subText = [i for i in subText if (i not in string.punctuation)]
        stop_words = stopwords.words('russian')
        stop_words.extend(['что', 'это', 'так', 'вот', 'быть', 'как', 'в', 'во', 'уж', '—', 'к', 'на', 'ко'])
        subText = [i for i in subText if (i not in stop_words)]
        characteristic = []
        for j in subText:
            p = morph.parse(j)
            pos = p[0].tag.POS
            # Характеристика строится на основе прилагательных
            if (pos == "ADJF" or pos == "ADJS"):
                characteristic.append(j)
        arr[was_names[_]]["characteristic"].append(characteristic)
    was_names = []

pprint(arr)

