lst=list(map(int,input("enter numbers sith space separated").split()))
for i in range(len(lst)):
    for  j in range(0,len(lst)-i-1):
        if lst[j]>lst[j+1]:
            temp=lst[j+1]
            lst[j+1]=lst[j]
            lst[j]=temp

print('the smallet no in list is=',lst[-1])