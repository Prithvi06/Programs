String=input("enter strings separated with Space")
s = String.split(' ')
for word in s:
    if len(word) % 2 == 0:
        print(word)
