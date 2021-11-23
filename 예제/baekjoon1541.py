temp = input()
answer = 0
if "-" not in temp:
    for i in temp.split("+"):
        answer += int(i)
    print(answer)
else:


    temp = temp.split("-")
    print(temp)


    answer = int(temp[0])
    for i in temp[1:]:
        zoogen = i.split("+")
        for j in zoogen:
            answer -= int(j)
    print(answer)