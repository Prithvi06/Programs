matrix = [[1, 4, 5], [7, 3], [4], [46, 7, 3]]
ans=1
for mat in matrix:
    for val in mat:
        ans=val*ans
print(ans)