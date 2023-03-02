matrix = [["wangoes", "good"], ["technology", "for"], ["Best"],['company','fresher']]
concat=[]
n=len(matrix[0])
for i in range(len(matrix[0])):
    con=''
    for j in  range(len(matrix)):
        if i<len(matrix[j]):
            con+=matrix[j][i]+' '

    concat.append(con)
print(concat)