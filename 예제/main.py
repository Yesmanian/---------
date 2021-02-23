i =63

a = ""
a+=str(i // 60*60) #시간
print(a)
a+=str((i%(60*60))//60) #분
print(a)
a+=str(((i%(60*60))%60))#초
print(a)
print(63 // (60*60))