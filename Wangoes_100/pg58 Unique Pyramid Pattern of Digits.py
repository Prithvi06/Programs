r=0
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=' ')
        r=j

    for k in range(r-1,0,-1):
        print(k,end=' ')

    print()