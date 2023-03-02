for i in range(11):
    for j in range(11):
        if (i==0) and (j in [1,2,3,7,8,9]):
            print('*',end=' ')
        elif (i==1 ) and (j in [0,4,6,10]):
            print('*',end=' ')
        elif (i in [2,3,4,5] ) and (j in [0,10]):
            print('*', end=' ')
        elif i==6 and (j in [1,9]):
            print('*', end=' ')
        elif i == 7 and (j in [2,8]):
            print('*', end=' ')
        elif i == 8 and (j in [3, 7]):
            print('*', end=' ')
        elif i == 9 and (j in [4, 6]):
            print('*', end=' ')
        elif i in [10,2] and j==5:
            print('*', end=' ')
        else:
            print(" ",end=' ')
    print()