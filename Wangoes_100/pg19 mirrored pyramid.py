n=int(input("enter lenght of pyramid"))
for row in range(1, n):
    num = 1
    for j in range(n, 0, -1):
        if j > row:
            print(' ', end=' ')
        else:
            print(num, end=' ')
            num += 1
    print('')