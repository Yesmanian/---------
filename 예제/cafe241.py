
args = ["a", "aaa", "bb", "ab", "cc", "cba", "a"]
def solution(args):

    args = list(set(args))

    print(args)
    args.sort(key=lambda x : (len(x),x))
    print(args)
    answer = []
    cnt = len(args[1])
    temp = []
    for i in args:
        if len(i) == cnt:
            temp.append(i)
        else:
            temp.reverse()
            for j in temp:
                answer.append(j)
            temp = [i]
            cnt = len(i)
    temp.reverse()
    for j in temp:
        answer.append(j)
    return answer



print(solution(args))


["a", "cc", "bb", "ab", "cba", "aaa"]