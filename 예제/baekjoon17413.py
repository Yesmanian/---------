s= '<   space   >space space space<    spa   c e>'

temp = []
answer = ''
# 1 가로안 2 가로 밖
gizun = 2
for i in s:
    if i == ' ' and gizun == 2:

        answer += "".join(list(reversed(temp)))
        answer += i
        temp = []
        continue

    if i == '<':

        answer += "".join(list(reversed(temp)))
        answer += i
        gizun = 1
        temp = []
        continue
    if i == '>':
        answer += i
        gizun = 2
        continue
    if gizun == 2:
        temp.append(i)
    else:
        answer+= i
answer += "".join(list(reversed(temp)))
print(answer)

