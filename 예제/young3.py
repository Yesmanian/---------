

# for _ in range(2):
#     score += int(input())
# print(score)

a = int(input())
b = int(input())
score = (a+b)/2
if a == 0 or b == 0:
    print("F")
elif 80 <= score < 100:
    print("A+")
elif 60 <= score:
    print("A0")
elif 40 <= score:
    print("B+")
else:
    print("B0")