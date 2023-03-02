string=input("enter strings")
list_string = string.split(' ')
new_str=''
for word in list_string:
    new_str+=word+'-'

print(new_str)