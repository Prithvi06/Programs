input=input("enter strings")
d=3

Lfirst = input[0: d]
Lsecond = input[d:]
Rfirst = input[0: len(input) - d]
Rsecond = input[len(input) - d:]

print("Left Rotation : ", (Lsecond + Lfirst))
print("Right Rotation : ", (Rsecond + Rfirst))