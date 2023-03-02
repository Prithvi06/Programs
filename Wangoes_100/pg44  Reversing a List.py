lst=list(map(int,input("enter numbers sith space separated").split()))
lst2=[]
for i in range(len(lst)-1,-1,-1):
    lst2.append(lst[i])
print(lst2)