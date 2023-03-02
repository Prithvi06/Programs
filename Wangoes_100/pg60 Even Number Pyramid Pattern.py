rows=int(input("enter rows"))
last_even= 2 * rows
evenNumber = last_even

for i in range(1, rows+1):
    evenNumber = last_even

    for j in range(i):
        print(evenNumber, end=' ')
        evenNumber -= 2

    print()