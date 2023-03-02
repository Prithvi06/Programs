keys_values= ((100,'wangoes',10000),(200,'is',20000),(300,'Best',30000))
lst=[]
keys=input("enter three key value").split()

for val in keys_values:
        print(val)
        dic={}
        dic[keys[0]]=val[0]
        dic[keys[1]]=val[1]
        dic[keys[2]]=val[2]
        lst.append(dic)
print(lst)
