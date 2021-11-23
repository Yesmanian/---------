
numbers =[4, 5, 11]



def solution(numbers):

    word = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    newList = []

    for i in numbers:
        i = str(i)
        temp = ""
        for j in i:
            temp+=word[int(j)]
        newList.append(temp)

    print(newList)
    tempList =[]
    for i in range(len(newList)):
        tempList.append([newList[i],numbers[i]])
    print(tempList)

    # for i in numbers:
    #    newList.append(word[int(str(i)[0])])


    tempList.sort()
    print(tempList)


    answer = []

    for i in tempList:
        answer.append(i[1])

    # for i in newList:
    #     for j in range(0,len(word)):
    #         if i == word[j]:
    #             answer.append(j)



    return answer

print(solution(numbers))