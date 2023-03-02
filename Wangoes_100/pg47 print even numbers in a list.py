lst=list(map(int,input("enter numbers sith space separated").split()))
lst2=[]
for n in lst:
    if n%2==0:
        lst2.append(n)

print('even number list',lst2)