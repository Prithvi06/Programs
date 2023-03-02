special=['@','_','!','#','$','%','^','&','*','(',')','<','>','?','/','\\','}','{','~',':',']']
String=input("enter string")
res=True
for c in String:
    if c in special:
        res=False
        break

if res==True:
    print("Acepted string doesnt contain special character")
else:
    print("not accepted strinng contain special character")