def trump_tweet(text) :
    # 주어진 규칙에 맞추어 trump_twit()함수를 구현해주세요.
    # pass는 지우고 코드를 작성해주세요.
    hashlist =[]
    mentionlist = []
    textlist = []
    tempList = text.split(" ")
    print(tempList)
    for i in tempList:
        if i[0] == '@':
            mentionlist.append(i[1:])
        elif i[0]== '#':
            hashlist.append(i[1:])
        else:
            textlist.append(i)
    print("hash list : ",hashlist)
    print("mention list : ",mentionlist)
    print("text list : ",textlist)



# 아래 부분은 수정하지 마세요!
# 입력과 출력을 수행하는 코드입니다.
t = "Make America Great Again @Trump #Speech #White_HOuse"
trump_tweet(t)

# hash list : ['Speech', 'White_HOuse']
# mention list : ['Trump']
# text list : ['Make', 'America', 'Great', 'Again']