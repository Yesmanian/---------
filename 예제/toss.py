import math
orderAmount =120
taxFreeAmount =20
serviceFee = 0

def solution(orderAmount, taxFreeAmount, serviceFee):
    # orderAmount : 주문금액
    # taxFreeAmount : 비과세금액
    # serviceFee : 봉사료
    answer = 0
    supply = 0

    if serviceFee == 0:
        supply = orderAmount
    else:
        supply = (orderAmount - serviceFee)
        if supply == 1:
            return answer

    #answer = (((supply + 0.1 * taxFreeAmount) / 1.1) - taxFreeAmount) * 0.1
    answer = ((supply - serviceFee) / 11 )
    print(answer)
    temp = answer - int(answer)
    if   temp < 0.1:
        return int(answer)
    else:
        return int(answer)+1
    print(temp)


    return answer

print(solution(orderAmount, taxFreeAmount, serviceFee))
print(math.ceil(12.01))