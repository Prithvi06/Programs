rows=int(input('enter rows no'))
for i in range(rows,0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print(' ')