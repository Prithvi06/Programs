lst=list(map(int,input("enter no separated by space").split()))
x=int(input("enter no for search"))
count=0
for ele in lst:
    if (ele == x):
        count = count + 1
print(count)