x=int(input('enter first number'))
y=int(input('enter second number'))
if x<y:
    hh=x
else:
    hh=y
for h in range(hh,0,-1):
    if (x%h==0 and y%h==0):
        hcf=h
        break

print(hcf)