lst=list(map(int,input("enter numbers sith space separated").split()))
psl=[]
ngl=[]
for n in lst:
    if n>=0:
        psl.append(n)
    else:
        ngl.append(n)
print('positive number list',psl)
print('negative number list',ngl)