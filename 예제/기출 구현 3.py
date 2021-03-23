#aabbaccc
def solution(b):
    answer = []
    for i in range(1, len(b) // 2 + 1):
        cnt = 1
        ans = ""
        s = b
        if s[:i] == s[i:2 * i]:
            while s:
                if s[:i] != s[i:2 * i]:
                    if cnt == 1:
                        ans += s[0]
                        s = s[1:]
                    else:
                        ans += str(cnt) + s[:i]
                        s = s[i:]
                        cnt = 1

                if s[:i] == s[i:2 * i]:
                    cnt += 1
                    s = s[i:]

            answer.append(len(ans))

    if answer == []:
        return len(b)
    else:
        return min(answer)