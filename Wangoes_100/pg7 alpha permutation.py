string='ABC'
m_list=[]
m_list.append(string)
t_list=[]
for i in range(len(string)-1):
    for word in m_list:
        for j in range(i,len(word)):
            word=list(word)
            word[i],word[j]=word[j],word[i]
            nword=''.join(word)
            t_list.append(nword)
    m_list=t_list
    t_list=[]

print(m_list)

#output
#['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']
