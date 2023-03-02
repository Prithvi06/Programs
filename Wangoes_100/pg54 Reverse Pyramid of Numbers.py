rows = int(input("enter rows no"))
for row in range(1, rows):
    for column in range(row, 0, -1):
        print(column, end=' ')

    print(' ')