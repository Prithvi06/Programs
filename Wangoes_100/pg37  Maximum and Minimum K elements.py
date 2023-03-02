tupl=(5, 20, 3, 7, 6, 8)
k=int(input('enter no to find min and max value'))
tupl=sorted(tupl)
llist=[]
llist.append(tupl[:k])
llist.append(tupl[-k:])
print(llist)