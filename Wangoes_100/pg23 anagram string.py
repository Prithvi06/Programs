a=input("Enter string 1:")
b=input("Enter string 2:")
count=0
for i in a:
    for j in b:
        if i==j:
            count=count+1

if count==len(a):
    print("string is anagram")
else:
    print("string is not anagram ")