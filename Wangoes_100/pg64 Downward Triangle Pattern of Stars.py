size=int(input("enter size of triangle"))
m = ((2 *size)-2)//2
for i in range(size,-1,-1):
    for j in range(0, m):
        print(' ', end='')
    m = m+1
    for j in range(0, i):
        print('*',end=' ')

    print(' ')