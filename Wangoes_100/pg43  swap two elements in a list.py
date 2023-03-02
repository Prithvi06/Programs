lst=list(map(int,input("enter numbers sith space separated").split()))
p1=int(input('enter one position'))
p2=int(input('enter second position'))
temp=lst[p1]
lst[p1]=lst[p2]
lst[p2]=temp
print(lst)