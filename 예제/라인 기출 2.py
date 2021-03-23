inp_str = "CaCbCgCdC888834A"

def solution(inp_str):
    answer = []
    #1
    if not 8<= len(inp_str) <= 15:
        answer.append(1)
    #5
    list_inp_str = list(inp_str)
    for i in list_inp_str:
        if list_inp_str.count(i) >= 5:
            answer.append(5)
    #4
    for i in range(0,len(list_inp_str)-3):
        count = 1
        for _ in range(3):
            if list_inp_str[i] == list_inp_str[i+1]:
                count +=1
        if count == 4:
            answer.append(4)
            break
    #2,3
    special = ['~','!','@','#','$','%','^','&','*']
    condition = [False,False,False,False]
    for i in list_inp_str:

        if i.isdigit():
            condition[2] = True

        if i in special:
                condition[3] = True

        if  65 <= ord(i) <= 90:
            condition[0] = True

        if  97 <= ord(i) <= 122:
            condition[1] =  True

        if i.isdigit() == False and not (65 <= ord(i) <= 90) and not (97 <= ord(i) <= 122) and i not in special:
            answer.append(2)





    count = 0
    for j in condition:
        if j == True:
            count +=1
    if count <= 2:
        answer.append(3)

    answer=list(set(answer))

    if answer == []:
        return [0]
    return answer

print(solution(inp_str))