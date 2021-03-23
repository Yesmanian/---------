program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]


# 각 command에 대한 boolean값 return매소드
def check(i, program,rules):
    # program명령어 확인
    if i[0] != program:
        return False

    checkList = []
    checkList2 = []
    for j in range(1,len(i)):
        if i[j][0] == '-':
            checkList.append(j)
    print(checkList)


    for k in range(len(checkList)):
        if k == len(checkList)-1:
            temp= i[checkList[k]:]
        else:
            temp = i[checkList[k]:checkList[k+1]]
        checkList2.append(temp)

    print(checkList2)

    for k in checkList2:
        for j in rules:
            if k == j[0]:
                if rules[0][0] == 'NUMBER' or 'STRING':
                    if len(k) != 2:
                        return False




    return True


def solution(program, flag_rules, commands):
    answer = []
    rules = []  # flag_rules list
    newCommands = []  # commands list
    # flag_rules를 list로 변환
    for i in flag_rules:
        temp = i.split()
        rules.append(temp)
    # commands를 list로 변환
    for i in commands:
        newCommands.append(i.split())
    # 각 command를 check메서드로 확인
    for i in newCommands:
        answer.append(check(i, program,rules))

    print(rules)
    print(newCommands)

    return answer

print(solution(program,flag_rules,commands))