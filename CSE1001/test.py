lis = [2, 2, 2, 6, 7, 8, 8]
n = len(lis)
i = 0
while i<n-1:
    if lis[i]==lis[i+1]:
        del lis[i+1]
        n -= 1
    else:
        i+=1

print(*lis)