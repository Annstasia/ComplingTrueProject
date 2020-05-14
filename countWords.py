import math
import string
from collections import Counter
from nltk.corpus import stopwords
from pprint import pprint

import nltk
import pymorphy2
with open("text_wihout_punctuation.txt", mode="r", encoding="utf-8") as file:
    text = file.read().lower()
def foo(text):
    words = nltk.word_tokenize(text)
    morph = pymorphy2.MorphAnalyzer()
    words1 = []

    stop_words = set(stopwords.words("russian"))
    # print(stop_words)
    for i in words:
        parsed = morph.parse(i)
        lemma = parsed[0].normal_form
        if (lemma not in stop_words):
            words1.append(lemma)
    return words1
    # countTfIdf(words1)

def countTF(text):
    tf_text = Counter(text)
    for i in tf_text:
        tf_text[i] = tf_text[i] / float(len(text))
    return tf_text

def countIDF(word, words1):
    return math.log10(len(words1)/sum([1.0 for i in words1 if word in i]))

def countTfIdf(corp):
    documents_list = []
    for text in corp:
        words1 = foo(text)
        tf_idf_dict={}
        tf_texts = countTF(words1)
        for i in tf_texts:
            tf_idf_dict[i] = tf_texts[i] * countIDF(i, words1)
        documents_list.append(tf_idf_dict)
    pprint(documents_list)
    return documents_list

path = 'bil1/'
corp = []
for name in range(1, 41):
    spans = {}
    # по очереди открываем файлы и извлекаем имена
    with open(path + str(name), 'r', encoding='utf-8') as f:
        text = f.read()
        for i in string.punctuation+"<«>»-—":
            text = text.replace(i, " ")
        corp.append(text)

documents_list = countTfIdf(corp)
to_write = ""
for i in range(len(documents_list)):
    to_write += "Текст " + str(i + 1) + "\n"
    for j in documents_list[i]:
        to_write += "\t" + j + " " +str(documents_list[i][j]) + "\n"
with open("tfIdfCount.text", mode="w", encoding="utf-8") as f:
    f.write(to_write)


