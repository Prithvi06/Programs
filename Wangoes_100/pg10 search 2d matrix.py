#sorted matrix
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=int(input('inter target'))
r=0
c=len(matrix)-1
while(r<len(matrix) and c>=0):
    if matrix[r][c]==target:
        print("True")
        break
    if matrix[r][c]>target:
        c-=1
    else:
        r+=1
else:
    print("False")

