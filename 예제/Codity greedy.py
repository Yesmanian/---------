A = [1, 3, 7, 9, 9]
B = [5, 6, 8, 9, 10]

def solution(A, B):
    result = 0
    for i in range(len(A)-1):
        a,b = A[i],B[i]
        count = 0
        for j in range(i+1,len(A)):
            a2,b2 = A[j],B[j]
            if a2 > a:
                count+=1
        if count >= result:
            result = count

    return result
print(solution(A,B))