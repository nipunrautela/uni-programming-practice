lis1 = [[1,2,3], [4,5,6], [7,8,9]]
lis2 = [[11, 12, 13], [14, 15, 16], [17, 18, 19]]
lis3 = [[], [], []]
for i in range(3):
    for j in range(3):
        sum = lis1[i][j] + lis2[i][j]
        lis3[i].append(sum)
print(*lis3)