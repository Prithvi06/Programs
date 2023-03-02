r=0
for i in range(6):
    for j in range(5,i,-1):
        print(j,end=' ')
        r=j

    for k in range(r,6):
        print(k,end=' ')

    print()