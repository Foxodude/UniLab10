# -*- coding: utf-8 -*-

import json

with open("1.json", encoding='utf-8') as file:
    products = json.load(file)

productsList = products["products"]
x = len(productsList)
for i in range(0, x):
    if productsList[i]["available"] == True:
        flag = "avaliable"
    else:
        flag = "Not available"
    stringToPrint = "имя: " + productsList[i]["name"] + "; цена: " + str(productsList[i]["price"]) + "; доступность: " + flag + "; вес: " + str(productsList[i]["weight"])
    print(stringToPrint)


userNameOfProduct = input("Введите название нового продукта: ")
userPriceOfProduct = input("Введите цену нового продукта: ")
userWeightOfProduct = input("Введите вес продукта: ")
shortName = {"Название": userNameOfProduct, "Цена": userPriceOfProduct, "Вес": userWeightOfProduct}
data = json.load(open("1.json"))
data["products"].append(shortName)
with open("1.json", "w") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

dictenRU = {}
dictruEN = {}
keyss = []
valuess = []
with open("en_RU.txt", "r", encoding="utf-8") as file:
        for line in file:
            pairsArray = line.split(",")                #Вместо сплита по \n
        for pair in pairsArray:
            keyValue = []
            keyValue = pair.split(" - ")
            keyss.append(keyValue[0])
            valuess.append(keyValue[1])
            # for letter in range(len(pair)):           #СТАРЫЙ ВАРИАНТ#
            #     maxi = len(pair)                      #СТАРЫЙ ВАРИАНТ#
            #     if pair[letter] == "-":               #СТАРЫЙ ВАРИАНТ#
            #         a.append(pair[0:letter])          #СТАРЫЙ ВАРИАНТ#
            #         b.append(pair[letter + 1:maxi])   #СТАРЫЙ ВАРИАНТ#
            dictenRU[keyValue[1]] = keyValue[0]
            dictruEN[keyValue[0]] = keyValue[1]
dict(sorted(dictruEN.items()))
resultative = str()
for i in dictruEN.items():
    resultative += i[0] + " - " + i[1] + "\n"
file1 = open('ru_EN.txt', 'w')
file1.write(resultative)