n =10
v1 =[1, 10, 6, 5, 6, 9]
v2 =[3, 7, 2, 8, 7, 3]
num =[3, 4, 5, 1, 8, 7, 9, 2]
amount=[10, 5, 6, -6, -8, 2, -2, 5]

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return  parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b :
        parent[b] = a
    else:
        parent[a] = b

def solution(n, v1, v2, num, amount):

    e = len(v1)

    parent = [0] * (n + 1)

    for i in range(1,n+1):
        parent[i] = i

    for i in range(e):
        a = v1[i]
        b = v2[i]
        union_parent(parent,a,b)

    team = []
    teamNo = []
    for i in range(1, n+1):
        team.append(find_parent(parent,i))
    print(team)
    for i in team:
        if i not in teamNo:
            teamNo.append(i)
    print(teamNo)

    teamNo2 = []
    for i in teamNo:
        teamNo2.append([i,0])

    print(teamNo2)


    for i in range(len(num)):
        teamGrade = team[num[i]-1]
        grade = amount[i]
        for i in teamNo2:
            if i[0] == teamGrade:
                i[1]+=grade
    print(teamNo2)
    teamNo2.sort(key = lambda x: (-int(x[1]),int(x[0])))
    print(teamNo2)
    answer = teamNo2[0][0]
    return answer

print(solution(n,v1,v2,num,amount))