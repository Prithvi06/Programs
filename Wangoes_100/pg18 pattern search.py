txt=input("enter text")
pat=input("enter pattern find")
for i in range(len(txt)):
    if pat==txt[i:len(pat)+i]:
        print("patern fount at index",i)