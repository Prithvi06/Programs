string=input("enter string")
k=int(input("mirror the characters from the N-th position  "))

original = 'abcdefghijklmnopqrstuvwxyz'
reverse = 'zyxwvutsrqponmlkjihgfedcba'
dictChars = dict(zip(original, reverse))

prefix = string[0:k - 1]
suffix = string[k - 1:]
mirror = ''

for i in range(0, len(suffix)):
    mirror = mirror + dictChars[suffix[i]]


print(prefix + mirror)