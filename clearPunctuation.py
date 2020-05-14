import string


to_save = ""
if __name__ == "__main__":
    path = 'bil1/'
    for name in range(1, 41):
        spans = {}
        # по очереди открываем файлы и извлекаем имена
        with open(path + str(name), 'r', encoding='utf-8') as f:
            text = f.read()
            for i in string.punctuation+"<«>»-—":
                text = text.replace(i, " ")
            to_save+= text
    with open("warpeace1.txt", 'r', encoding='cp1251') as f:
        text = f.read()
        for i in string.punctuation+"<«>»-—":
            text = text.replace(i, " ")
        to_save+= text
    print(to_save)
    file_to_save = open("warAndPeace_wihout_punctuation1.txt", mode="w", encoding="utf-8")
    file_to_save.write(to_save)
            # print(text)
        # words = nltk.word_tokenize(text)
        # for i in words:
        #     print(i)
            # tokens1 = f.read().split()
        # tokens1 = filter_stopwords(tokens1)
        # count_frequencies(tokens1)
        # print()


    # with open("Texts/unknown1.txt", 'r', encoding='utf-8') as f:
    #     tokens1 = f.read().split()
    # with open("Texts/unknown2.txt", 'r', encoding='utf-8') as f:
    #     tokens2 = f.read().split()
    # with open("Texts/unknown3.txt", 'r', encoding='utf-8') as f:
    #     tokens3 = f.read().split()
    # with open("Texts/unknown4.txt", 'r', encoding='utf-8') as f:
    #     tokens4 = f.read().split()
    # tokens1 = filter_stopwords(tokens1)
    # tokens2 = filter_stopwords(tokens2)
    # tokens3 = filter_stopwords(tokens3)
    # tokens4 = filter_stopwords(tokens4)
    # count_frequencies(tokens1)
    # print()
    # count_frequencies(tokens2)
    # print()
    # count_frequencies(tokens3)
    # print()
    # count_frequencies(tokens4)
