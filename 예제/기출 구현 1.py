array = list(map(int,input()))

arrayLeft = array[:len(array)//2]
arrayRight = array[len(array)//2:]

if sum(arrayLeft) == sum(arrayRight):
    print("YEs")
else:
    print("No")

print(arrayLeft)
print(arrayRight)
