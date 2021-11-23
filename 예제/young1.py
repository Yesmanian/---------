middleInput = input()

size = len(sentence)
# print(size)
sentenList = list(sentence)

sentenList.insert(size//2,middleInput)

# print(sentenList)
sentence = "".join(sentenList)