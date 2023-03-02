x=int(input('enter first number'))
y=int(input('enter second number'))
if x>y:
    mx=x
else:
    mx=y
while (True):
    if ((mx % x == 0) and (mx % y == 0)):
        lcm = mx
        break
    mx += 1
print(lcm)