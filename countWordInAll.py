from collections import Counter
from nltk.corpus import stopwords
from pprint import pprint
import string

import nltk
import pymorphy2
def foo(text, name):
    words = nltk.word_tokenize(text)
    morph = pymorphy2.MorphAnalyzer()
    words1 = []
    q = 0

    stop_words = set(stopwords.words("russian"))
    print(stop_words)

    for i in words:
        parsed = morph.parse(i)
        lemma = parsed[0].normal_form
        # print(lemma)
        if (lemma not in stop_words):
            words1.append(lemma)
            q+=1
    freq = Counter(words1)
    string=""
    k = 1
    for i in sorted(freq, key=lambda s: -freq.get(s)):
        if (i != None and freq.get(i) != None):
            string += str(k) + "\t" + i + "\t" + str(freq.get(i)) + "\t" + str(round(freq.get(i) / q, 3)) + "\n"
            k += 1
    print(string)
    with open(name, mode="w", encoding="utf-8") as f:
        f.write(string)

    # pprint(freq)
    # print(q)

path = 'bil1/'
corp = []
allTexts = ""
for name in range(1, 41):
    spans = {}
    # по очереди открываем файлы и извлекаем имена
    with open(path + str(name), 'r', encoding='utf-8') as f:
        text = f.read().lower()
        for i in string.punctuation+"«»–—":
            text = text.replace(i, " ")
    allTexts+="\n" + text
foo(allTexts, "countAllWords.txt")
# foo("warAndPeace_wihout_punctuation1.txt", string.punctuation)
