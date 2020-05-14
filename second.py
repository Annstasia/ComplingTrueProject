import json
import pprint


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
    "мур": None,
    "сафат": None,
    "сафет": None,
    "наезжай": None,
    "здымаленькая": None,
    "ида": None,
    "расставимша": None
}

middleDict={
    "никитиевич": "никитич",
    "олександровна": "александровна"
}

lastDictionary={

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
    "белых": None,
    "единое": None,
    "поповигший": None,
    "скоморошин": None,
    "никитинич": "никитич"




}


lastShouldFirst = {
    "микула": "микула",
    "добрынин": "добрыня",
    "добрынинын": "добрыня",
    "микулов": "микула",
    "маринин": "маринка",
    "алешенек": "алеша",
    "еким": "еким",
    "ильюшенка": "илья",
    "олеша": "алеша",
    "алешин": "алеша"



}

fullNamesDict={
    "алеша None None": "алеша None попович",
    "None None попович": "алеша None попович",
    "владимир None None": "владимир None князь",
    "тугарин None None": "тугарин None змей",
    "тугарин змеевич None": "тугарин None змей",
    "None None змеевич": "тугарин None змей",
    "None None тугаринов": "тугарин None змей",
    "тугарин None змеевич": "тугарин None змей",
    "тугаретин None None": "тугарин None змей",
    "None None тугарин": "тугарин None змей",
    "None None тугаретина": "тугарин None змей",

    "еким None None": "еким None иванович",
    "добрыня None None": "добрыня None никитич",
    "добрыня никитич None": "добрыня None никитич",
    "офимья None None": "офимья None александровна",
    "None None муромец": "илья None муромец"


}


with open("fileJson1.json", "r") as read_file:
    newData = json.load(read_file)

# newData = {}
was = False

def changeName(name):
    # print(name)
    first, middle, last = name.split()
    first = str(namesDict.get(first, first))
    middle = str(middleDict.get(middle, middle))
    if last in lastShouldFirst:
        if first != "None":
            if (first == "иванович" and last== "еким"):
                first, last = last, first
            else:

                print("Error!!!", first, last)
                return None
        else:

            first = str(lastShouldFirst[last])
            last = "None"
    else:
        last = str(lastDictionary.get(last, last))
    new_name = first + " " + middle + " " + last
    if new_name in fullNamesDict:
        return fullNamesDict[new_name]
    return first + " " + middle + " " + last


# for i in data:
    # first, middle, last = i.split()
    # name = changeName(i)
    # if (name == "None None None"):
    #     continue
    # if (name == None):
    #     break
    # if (name not in newData):
    #     newData[name] = {"names": {}, "characteristic": [], "count": 0}
    # newData[name]["characteristic"].append(data[i]["characteristic"])
    # newData[name]["count"] += data[i]["count"]
    # for j in data[i]["names"]:
    #     new_name = changeName(j)
    #     if (new_name == "None None None"):
    #         continue
    #     if (new_name != None):
    #
    #         # print(newData)
    #         # print(newData[name]["names"].get(new_name, 0))
    #         if new_name not in newData[name]["names"]:
    #             newData[name]["names"][new_name] = [0, []]
    #         newData[name]["names"][new_name][0] += 1
    #         for q in data[i]["names"][j][1]:
    #             if q not in newData[name]["names"][new_name][1]:
    #                 newData[name]["names"][new_name][1].append(q)
    #         # if new_name in newData[name]["names"]:
    #         #     newData[name]["names"][newData] += 1
    #         # else:
    #         #     newData[name]["names"][newData] = 1
    #         # newData[name]["names"].append(new_name)
    #     else:
    #         was = True
    #         break
    #     if was:
    #         break



def showNames():
    for i in sorted(newData, key=lambda s: -newData[s]["count"]):
        print(i)

def showNameDict():
    for i in newData:
        print(i)
        for j in sorted(newData[i]["names"], key=lambda s: -newData[i]["names"][s][0]):
            print("\t", j, newData[i]["names"][j])
        print(newData[i]["count"])
        inp = input()
        if (inp == "q"):
            return

def showSomeName(name):
    print(name, "names")
    for j in newData[name]["names"]:
        print("\t", j, newData[name]["names"][j])
    print(name, "character")
    for j in newData[name]["characteristic"]:
        print("\t", j)
    for j in newData[name]["smallCharacteristic"]:
        print("\t", j)


def showComment():
    for i in newData:
        print(i)
        for j in newData[i]["characteristic"]:
            print(j)
        inp = input()
        if (inp == "q"):
            return

def showSmallComment():
    for i in newData:
        print(i)
        for j in newData[i]["smallCharacteristic"]:
            print(j)
        inp = input()
        if (inp == "q"):
            return


pprint.pprint(newData)
while True:
    inp = input()
    if inp == "1":
        showNames()
    elif inp == "2":
        showNameDict()
    elif inp == "4":
        showComment()

    elif inp == "5":
        showSmallComment()

    elif inp.split()[0] == "3":
        showSomeName(inp[2:])











# pprint.pprint(data)