info = []
max_total = 0
index = 0
for i in range(5):
    name = input()
    regno = int(input())
    marks1 = int(input())
    marks2 = int(input())
    marks3 = int(input())
    info.append((name,regno,[marks1,marks2,marks3]))
    if marks1+marks2+marks3 > max_total:
        max_total = marks1+marks2+marks3
        index = i
print(info[i][0])
print(max_total)
    
