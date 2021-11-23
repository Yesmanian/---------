
ings = ["r 10", "a 23", "t 124", "k 9"]
menu = ["PIZZA arraak 145", "HAMBURGER tkar 180", "BREAD kkk 30", "ICECREAM rar 50", "SHAVEDICE rar 45", "JUICE rra 55", "WATER a 20"]
sell = ["BREAD 5", "ICECREAM 100", "PIZZA 7", "JUICE 10", "WATER 1"]

def solution(ings, menu, sell):
    answer = 0

    ingsList = []
    menuList = []
    sellList = []
    for i in ings:
        ingsList.append(i.split(" "))
    for i in menu:
        menuList.append(i.split(" "))
    for i in sell:
        sellList.append(i.split(" "))

    print(ingsList)
    print(menuList)
    print(sellList)

    index = 0
    for i in menuList:
        income = 0
        for j in i[1]:
            for k in ingsList:
                if k[0] == j:
                    income += int(k[1])
        menuList[index].append(int(i[2]) - income)
        index += 1

    for i in sellList:
        for j in menuList:
            if j[0] == i[0]:
                answer += (j[3] * int(i[1]))


    print(menuList)






    return answer

print(solution(ings,menu,sell))