table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]


def solution(table, languages, preference):
    newTable = []
    answer = []
    for i in table:
        temp = i.split()
        newTable.append(temp)


    for i in newTable:
        point = 0
        for h in range(1,6):
            for j in range(len(languages)):
                if i[h] == languages[j]:
                    point += (6 - h) * preference[j]
        answer.append((i[0],point))

    answer.sort(key=lambda x:(-x[1],x[0]))
    return answer[0][0]

print(solution(table,languages,preference))