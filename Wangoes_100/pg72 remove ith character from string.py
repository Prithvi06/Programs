strs = "Wangoes Technology"
pos=int(input("enter position to remove character"))
new_str = ""
for i in range(len(strs)):
    if i != 2:
        new_str = new_str + strs[i]

print("The string after removal of  character:", new_str)