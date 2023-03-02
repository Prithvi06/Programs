a=[-2,-3,4,-1,-2,1,5,3]
max_val=min(a)
print(min(a))
max_end=0
for  i in range(len(a)):
        max_end=max_end+a[i]
        if max_end>max_val:
            max_val=max_end
        if max_end<=0:
            max_end=0
print(max_val,start,end)
