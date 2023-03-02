string=input("enter string")
s1=input("enter word to be replace")
s2=input("replace word")

new_str=''
idx=string.find(s1)
if idx==-1:
    print("replace word nnot matched")
else:
     new_str=string[:idx]+s2+string[idx+len(s1):]

print(new_str)