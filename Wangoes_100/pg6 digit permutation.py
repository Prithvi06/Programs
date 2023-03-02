
input=[1,2,3]
m_list=[]
m_list.append(input)
t_list=[]
for i in range(len(input)-1):
    for words in m_list:
        for j in range(i,len(words)):
            word = words.copy()
            #print(word)
            word[i],word[j]=word[j],word[i]
            t_list.append(word)
            #print('tlist',t_list)
    m_list=t_list
    t_list=[]
    
print('mlist',m_list)
sort_list=sorted(m_list)
print(sort_list)

#output,
#[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
