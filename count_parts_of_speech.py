from collections import Counter
from nltk.corpus import stopwords
from pprint import pprint

import nltk
import pymorphy2
def foo(name):

    with open(name, mode="r", encoding="utf-8") as file:
        text = file.read().lower()
    words = nltk.word_tokenize(text)
    morph = pymorphy2.MorphAnalyzer()
    wordsDict = {}
    words1 = []
    q = 0

    stop_words = set(stopwords.words("russian"))
    print(stop_words)

    for i in words:
        parsed = morph.parse(i)
        lemma = parsed[0].normal_form
        # print(lemma)
        if (lemma not in stop_words):
            words1.append(parsed[0].tag.POS)
            q+=1
            # if q % 10000 == 0:
            #     print("введите enter")
            #     input()
    freq = Counter(words1)
    string=""
    for i in sorted(freq, key=lambda s: -freq.get(s)):
        if (i != None and freq.get(i) != None):
            string += i + "\t" + str(round(freq.get(i) / q, 3)) + "\n"
    with open("count_parts_" + name, mode="w", encoding="utf-8") as f:
        f.write(string)

    pprint(freq)
    print(q)


foo("text_wihout_punctuation.txt")
foo("warAndPeace_wihout_punctuation1.txt")

# k = 0
# to_write = ""
# for i in sorted(freq, key=lambda s: -freq.get(s)):
#     to_write += str(k) + "\t" + i + "\t" + str(freq.get(i)) + "\n"
#     k+= 1
# with open("count_words.txt", mode="w", encoding="utf-8") as file:
#     file.write(to_write)
#     # if (lemma in wordsDict):
#     #     wordsDict[lemma].add(i)
#     # else:
#     #     wordsDict[lemma] = set()
#     #     wordsDict[lemma].add(i)
#     # wordsDict[lemma] = wordsDict.get(lemma, set()).add(i)
# # print(wordsDict)
