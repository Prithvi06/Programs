test_list = [[4, 5, 6], [8, 1, 10], [7, 12, 5]]
print("The original list is : " + str(test_list))
k=2
res =[]

for i in range(len(test_list)):
    res.append(test_list[i][k])
print("The Kth column of matrix is : " + str(res))