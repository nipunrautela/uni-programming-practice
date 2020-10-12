stuNum = int(input("Enter the number of students in class: "))
total = 0
count = 0
while(count < stuNum):
    mark = float(input(f"Enter marks of student {count+1}: "))
    total += mark
    count += 1
    
print("Class Average: ", total/stuNum)
