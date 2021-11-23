
compressed = "10(p)"

def numList(compressed):
    stack = []
    stack2 = []
    for i in range(len(compressed)):
        if compressed[i] == '(':
            stack.append(i)
        if compressed[i] == ')':
            stack.append(i)
            return stack[-2:]

def solution(compressed):

    while '(' in compressed:
        startLast = numList(compressed)
        start = startLast[0]
        last = startLast[1]

        i = 1
        while compressed[start-i].isdigit():
            i += 1
        i -= 1
        multi = int(compressed[start-i:start])
        print(multi)


        back = compressed[last+1:]
        front = compressed[:start-len(str(multi))]
        compressed = front + multi * compressed[start+1:last] + back
    print(numList(compressed))
    print(compressed)





    answer = compressed
    return answer

solution((compressed))




# def numList(compressed):
#     stack = []
#     stack2 = []
#     for i in range(len(compressed)):
#         if compressed[i] == '(':
#             stack.append(i)
#         if compressed[i] == ')':
#             stack.append(i)
#             return stack[-2:]
#
# def solution(compressed):
#
#     while '(' in compressed:
#         startLast = numList(compressed)
#         start = startLast[0]
#         last = startLast[1]
#         multi = int(compressed[start-1])
#         back = compressed[last+1:]
#         front = compressed[:start-1]
#         compressed = front + multi * compressed[start+1:last] + back
#     # print(numList(compressed))
#     # print(compressed)
#
#
#
#
#
#     answer = compressed
#     return answer