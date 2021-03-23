def solution(N, stages):
    people = len(stages)
    stages.sort()
    ans = []

    for i in range(1,N+1):
        count = stages.count(i)
        ans.append((i,count/people))
        people -= stages.count(i)

    answer = []
    return ans


answer1 = solution(4,[4,4,4,4])
print(answer1)
answer1.sort(key= lambda x:-x[1])
print(answer1)
ans = []
for i in answer1:
    ans.append(i[0])
print(ans)
