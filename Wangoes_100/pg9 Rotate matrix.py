matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix.reverse()
for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                #temp=matrix[i][j]
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                #matrix[j][i]=temp

print(matrix)

#output
# [[7, 4, 1],
# [8, 5, 2],
# [9, 6, 3]]