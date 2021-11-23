
# arr =[3, 3, 3, 3, 3, 3]
# arr = [2, 1, 3, 1, 2, 1]
arr = [1, 2, 3]
def solution(arr):

    answer = []

    cnt123 = [arr.count(1),arr.count(2),arr.count(3)]
    max123 = max(cnt123)
    print(max123)
    print(cnt123)

    for i in cnt123:
        answer.append(max123 - i)





    return answer

print(solution(arr))