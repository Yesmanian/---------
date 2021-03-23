
program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]


# 각 command에 대한 boolean값 return매소드
def check(i, program):
    # program명령어 확인
    if i[0] != program:
        return False
    # flag와 flag_rule를 확인
    for j in range(1, len(i)):
        if i[j] == '-n':
            if not i[j + 1].isdigit():
                return False

        if i[j] == '-s':
            if not i[j + 1].isalpha():
                return False

        if i[j] == '-e':  # null값이 들어옴으로 리스트의 길이가 짝수이다
            if len(i) % 2 != 0:
                return False

        if '-e' not in i and len(i) % 2 == 0:  # flag가 존재하지 않으면 리스트의 길이가 짝수이다
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
        answer.append(check(i, program))

    return answer

print(solution(program,flag_rules,commands))
