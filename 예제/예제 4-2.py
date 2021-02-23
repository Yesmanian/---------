n = int(input())

count = 0

time = n*60*60+59*60+59

for i in range(1,time+1):
    a = ""
    a+=str(i // (60*60)) #시간
    a+=str((i%(60*60))//60) #분
    a+=str(((i%(60*60))%60))#초

    if '3' in a:
        count+=1
        print(a,i)
print(count)

# str = "33"
# for i in str:
#     if i == '3':
#         print(1)