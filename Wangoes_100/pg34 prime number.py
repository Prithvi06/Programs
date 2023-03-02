n= int(input( "enter the number that has to be checked:"))
a=0
for i in range(2,(n//2)+1):
    if(n%i == 0):
        a=a+1
if(a>1):
    print("it is not prime")
else:
    print("it is prime ")