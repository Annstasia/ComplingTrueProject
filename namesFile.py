import json
names= ['Алёша Попович',
        'Аника-воин',
        'Бова Королевич',
        'Василий Буслаев',
        'Василиса Микулишна',
        'Владимир Красное Солнышко',
        'Вольга Святославич',
        'Гаврила Алексич',
        'Горыня',
        'Дубыня',
        'Усыня',
        'Данило Игнатьевич',
        'Добрыня Никитич',
        'Дунай Иванович',
        'Дюк Степанович',
        'Евпатий Коловрат',
        'Жидовин',
        'Змей Горыныч',
        'Иван Гостиный сын',
        'Иван Данилович',
        'Идолище Поганое',
        'Илья Муромец',
        'Индрик',
        'Калин-царь',
        'Катерина Прекрасная',
        'Колыван',
        'Микула Селянинович',
        'Михайло Данилович',
        'Михайло Казарянин',
        'Михайло Потык',
        'Морской царь',
        'Настасья Микулишна',
        'Никита Кожемяка',
        'Поленица',
        'Полкан',
        'Садко',
        'Самсон',
        'Саур Ванидович',
        'Святогор',
        'Соловей Будимирович',
        'Соловей-разбойник',
        'Ставр Годинович',
        'Суровец',
        'Сухман Одихмантьевич',
        'Тугарин',
        'Хотен',
        'Чернава',
        'Чудо-юдо',
        'Чурило Плёнкович',
        'Ян Усмошвец']

roors = {
        "олеш": ['Алёша Попович'],
        "алеш": ['Алёша Попович'],
        "александр": ['Алёша Попович'],
        "попов": ['Алёша Попович'],

        "аник": ['Аника-воин'],

        "корол": ['Бова Королевич'],

        "васил": ['Василиса Микулишна', 'Василий Буслаев'],
        "бусл": ['Василий Буслаев'],
        "микулиш": ["Василиса Микулишна", "Настасья Микулишна"],

        "влад": ['Владимир Красное Солнышко'],
        "красн": ['Владимир Красное Солнышко'],
        "солн": ['Владимир Красное Солнышко'],

        "вольг": ['Вольга Святославич'],
        "свят": ['Вольга Святославич'],

        "гавр": ['Гаврила Алексич'],
        "алекс": ['Гаврила Алексич'],

        "горын": ['Горыня', 'Змей Горыныч'],
        "дуб": ["Дубыня"],
        "усы": ['Усыня'],

        "данило": ['Данило Игнатьевич'],
        "игнат": ['Данило Игнатьевич'],

        "добр": ['Добрыня Никитич'],
        "никити": ['Добрыня Никитич'],

        "дун": ['Дунай Иванович'],
        "ивано": ['Дунай Иванович'],

        "дюк": ["Дюк Степанович"],
        "степ": ['Дюк Степанович'],

        "евпат": ['Евпатий Коловрат'],
        "колов": ['Евпатий Коловрат'],

        "жид": ['Жидовин'],

        "зме": ['Змей Горыныч', "Тугарин"],
        "зми": ['Змей Горыныч', "Тугарин"],

        "идол": ['Идолище Поганое'],
        "полган": ['Идолище Поганое'],

        "иль": ['Илья Муромец'],
        "илю": ['Илья Муромец'],
        "муром": ['Илья Муромец'],

        "индр": ['Индрик'],
        'калин': ['Калин-царь'],
        'царь': ['Калин-царь', 'Морской царь'],

        'катерин': ['Катерина Прекрасная'],
        "прекрасн": ['Катерина Прекрасная'],

        "колы": ['Колыван'],

        "микул": ['Микула Селянинович'],
        "селян": ['Микула Селянинович'],

        "михай": ['Михайло Данилович', 'Михайло Казарянин', 'Михайло Потык'],
        "данил": ['Михайло Данилович', "Данило Ловчанин"],
        "казяр": ['Михайло Казарянин'],
        "потык": ['Михайло Потык'],

        "морск": ['Морской царь'],
        "настас": ['Настасья Микулишна'],
        "никит": ['Никита Кожемяка'],
        "сад": ['Садко'],
        "самс": ['Самсон'],
        "саур": ['Саур Ванидович'],
        "ванид": ['Саур Ванидович'],
        "святог": ['Святогор'],
        "солов": ['Соловей Будимирович', 'Соловей-разбойник'],
        "будимир": ['Соловей Будимирович'],
        "разбой": ['Соловей-разбойник'],
        "ставр": ['Ставр Годинович'],
        "суров": ['Суровец'],
        "сухман": ['Сухман Одихмантьевич'],
        "одихман": ['Сухман Одихмантьевич'],
        "тугар": ['Тугарин'],
        "хотен": ['Хотен'],
        "черна": ['Чернава'],
        "чудо": ['Чудо-юдо'],
        "юдо": ['Чудо-юдо'],
        "чурил": ['Чурило Плёнкович'],
        "пленк": ['Чурило Плёнкович'],
        "усмош": ['Ян Усмошвец'],
        "блуд": ["Хотен Блудович"],
        "иван": ["Иван Годинович", "Иван Гостиный Сын"],
        "годин": ["Иван Годинович","Ставр Годинович"],
        "ловча": ["Данило Ловчанин"],
        "глеб": ["Глеб Володьевич"],
        "володь": ["Глеб Володьевич"],
        "дуна": ["Дунай"],
        "мама": ["Мамай"]


}


names1 = [
        "Василий Буслаев",
        "Чурило Пленкович",
        "Хотен Блудович",
        "Соловей Будимирович",
        "Михайло Потык",
        "Иван Годинович",
        "Ставр Годинович",
        "Иван Гостиный Сын",
        "Данило Ловчанин",
        "Глеб Володьевич",
        "Василий Казимирович",
        "Дунай",
        "Мамай",


]

with open("fileJson2.json", "w", encoding="utf-8") as file:
    json.dump(roors, file, ensure_ascii=False)
print(names)
# print([(" ".join(i.split())).replace(",", "") for i in names[0].split('\n')])