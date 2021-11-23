# import heapq
#
# def solution(food_times,k):
#     if sum(food_times) <=k:
#         return -1
#
#     q=[]
#     for i in range(len(food_times)):
#         heapq.heappush(q,(food_times[i],i+1))
#
#     sum_value = 0
#     previous = 0
#     length = len(food_times)
#
#     while sum_value +  (q[0][0] - previous * length) <=k:
#         now = heapq.heappop(q)[0]
#         sum_value += (now - previous) *length
#         length -=1
#         previous = now
#
#     result = sorted(q,key= lambda x: x[1])
#     return result[(k-sum_value) % length]

#2
import heapq
food_times = [3, 1, 2]
k = 5
def solution(food_times, k):
    if sum(food_times) < k:
        return -1
    food = []
    for i in range(len(food_times)):
        heapq.heappush(food,(food_times[i],i+1))

    print(food)
    # print(heapq.heappop(food))
    # print(heapq.heappop(food))
    # print(heapq.heappop(food))

    time = 0
    print(food[0][0])
    heapq.heappop(food)[0]
    print(food)
    print(food[0][0])






    return 3


print(solution(food_times,k))