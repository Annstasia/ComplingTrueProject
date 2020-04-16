import os

# В файлах была кривая кодировка и лишняя информация. Выложенные в репозитрии файлы уже обработаны.
# Повторная обработка не нужна.
path = 'bil/'
for name in range(20):
    spans = []
    # по очереди открываем файлы и извлекаем имена
    with open(path + str(name) + "/" + str(name) + ".txt", 'r', encoding='cp1251') as f:
        text = f.read().strip()
        k1 = text.find("Приятного чтения!")
        k2 = text.find('''Спасибо, что скачали книгу в бесплатной электронной библиотеке TheLib.Ru: http://thelib.ru

Оставить отзыв о книге:''')
        text = text[k1 + 17:k2]
    file = open(path + str(name) + "/" + str(name) + ".txt", 'w', encoding='utf-8')
    file.writelines(text)
    file.close()