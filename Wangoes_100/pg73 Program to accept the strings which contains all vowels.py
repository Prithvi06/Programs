strs=input("enter strings")
vow=['a','e','i','o','u']
count=0
for c in strs:
    c=c.lower()
    if c in vow:
        count+=1
        vow.remove(c)

if count==5:
    print('string accepted CZ string contain all vowels')
else:
    print("not accepted  CZ string not contain all vowels")