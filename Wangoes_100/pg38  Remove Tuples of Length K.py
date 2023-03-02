t_list = [(4,5),(4,),(8,6,7),(1,) ,(3,4,6,7)]
res=[]
l=int(input("enter tuple length you want to remove"))
for tup in t_list:
    if len(tup)!=l:
        res.append(tup)

print(res)