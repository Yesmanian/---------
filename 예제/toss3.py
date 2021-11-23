
amountText = "10000"

def solution(amountText):
    answer = True


    if amountText[0] == '0':
        return False

    for i in range(len((amountText))):
        if i == 0:
            if amountText[i] == '0' or amountText[i] == ',':
                return False
        if i == len(amountText) and amountText[i] == ',':
            return False


        if amountText[i] != ',' and not amountText[i].isdigit():
            answer = False
            return answer

    if ',' in amountText:
        temp = ""
        for i in amountText:
            if i != ',':
                temp+=i
        temp = int(temp)
        temp = format(temp,",")
        print(temp)
        if temp == amountText:
            return True
        else:
            return False






    return answer

print(solution(amountText))

a=1234
print(a)
a = format(a,",")
print(a)