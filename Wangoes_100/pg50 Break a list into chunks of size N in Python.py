my_list = ['wangoes','team','work','intern','training','technology','skill','passion','python','django']
n=int(input('enter chunks of size'))
lst=[]
ls=[]
for word in my_list:
    ls.append(word)
    if len(ls)==n:
        lst.append(ls)
        ls=[]
if len(ls)>1:
    lst.append(ls)
print(lst)