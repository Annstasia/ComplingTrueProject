from collections import Counter
from nltk.corpus import stopwords
from pprint import pprint

import nltk
import pymorphy2
with open("text_wihout_punctuation.txt", mode="r", encoding="utf-8") as file:
    text = file.read().lower()

words = nltk.word_tokenize(text)
morph = pymorphy2.MorphAnalyzer()
wordsDict = {}
words1 = []

stop_words = set(stopwords.words("russian"))
print(stop_words)

for i in words:
    parsed = morph.parse(i)
    lemma = parsed[0].normal_form
    if (lemma not in stop_words):
        words1.append(i)
freq = Counter(words1)
pprint(freq)
k = 0
to_write = ""
for i in sorted(freq, key=lambda s: -freq.get(s)):
    to_write += str(k) + "\t" + i + "\t" + str(freq.get(i)) + "\n"
    k+= 1
with open("count_words.txt", mode="w", encoding="utf-8") as file:
    file.write(to_write)
#     # if (lemma in wordsDict):
#     #     wordsDict[lemma].add(i)
#     # else:
#     #     wordsDict[lemma] = set()
#     #     wordsDict[lemma].add(i)
#     # wordsDict[lemma] = wordsDict.get(lemma, set()).add(i)
# # print(wordsDict)
