a= ([0,0],[0,1],[0,2],[1,0])
print(a)
b = list(a)
b.sort(key =lambda x: (x[0],x[1]))
print(b)

x1,x2 = b[0]
print(x1,x2)