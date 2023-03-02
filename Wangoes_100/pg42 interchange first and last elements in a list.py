lst=list(map(int,input("enter numbers sith space separated").split()))
temp=lst[0]
lst[0]=lst[-1]
lst[-1]=temp
print(lst)