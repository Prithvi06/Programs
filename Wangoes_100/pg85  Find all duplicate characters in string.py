input=input("enter string")
WC={}
j=0
for c in input:
    if c not in WC:
        WC[c]=1
    else:
        WC[c]+=1
for i in WC:
    if (WC[i] > 1):
        print(i)

