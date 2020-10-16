# marks1 = int(input("Enter marks for subject 1: "))
# marks2 = int(input("Enter marks for subject 2: "))
# marks3 = int(input("Enter marks for subject 3: "))
    
# if 100 > marks1 < 0 or 100 >= marks2 < 0 or 100 >= marks3 < 0:
#     print("Invalid marks")
# else:
#     print("Average: ", (marks1+marks2+marks3)/3)
#     if marks1 >= 50 and marks2 >= 50 and marks3 >= 50:
#         print("Status: Pass")
#     else:
#         print("Status: Fail")

# Alternate method
marks = []
total = 0
status = "Pass"
subjects_count = int(float(input("Enter the number of subjects: ")))
for i in range(subjects_count):
    invalid = True
    tries = 3
    while invalid:
        if tries == 0:
            print("Out out tries, program will now exit!")
            exit()  
        tries -= 1
        mark = int(input(f"Enter marks for subject {i+1}: "))
        if mark > 100 or mark < 0:
            print(f"Invalid Marks. {tries} tries left.")
        else:
            invalid = False
    marks.append(mark)
    total += mark
    if mark < 50:
        status = "Fail"
    
print("Total: ", total)
print("Average: ", round(total/len(marks), 2))
print("Status: ", status)
    