string=input("enter string")
s={'0','1'}
st=set(string)
if st==s or s=={'0'} or s=={'1'}:
    print("string is binary")
else:
    print("string is not binary")