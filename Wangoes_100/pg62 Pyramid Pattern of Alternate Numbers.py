rows = int(input('enter rowss'))
k = 0
for i in range(1,rows+1):
    for j in range(i):
        print(i+k,end=' ')

    k=k+1
    print()