mat=[[1,2,3,],[4,5,6],[7,8,9],[10,11,12]]
transpose=[]
trans=[]
for i in range(len(mat[0])):
    trans=[]
    for j in range(len(mat)):
        trans.append(mat[j][i])
    transpose.append(trans)

for trans in transpose:
    print(trans)