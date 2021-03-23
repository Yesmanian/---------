n,m = map(int,input().split())
function = []
for _ in range(m):
    oper,a,b =map(int,input().split())
    array = [oper,a,b]
    function.append(array)

team = [[i] for i in range(n+1)]

for j in function:
    if j[0] == 0:
        team[j[0]].append(j[1])
        team[j[1]].append(j[0])
    else:
        if j[2] in team[j[1]]:
            print("YES")
        else:
            print("No")
print(team)