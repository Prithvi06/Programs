n=int(input("enter matrix size n*n"))
result=[]
a=1
for i in range(n):
    res=[]
    for j in range(n):
        res.append(a)
        a+=1
    result.append(res)
print(result)