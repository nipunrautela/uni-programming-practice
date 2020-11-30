n = int(input("Enter the number of students: "))
students = []

for i in range(n):
    student = {}
    student["name"] = input("Enter name of student {}: ".format(i+1))
    student["reg_no"] = input("Enter register number of student {}: ".format(i+1)).upper()
    students.append(student)

to_search = input("Enter the register number of student: ")
iterations = 0
for student in students:
    if student["reg_no"] == to_search.upper():
        print("Student found:", student["name"], "-", student["reg_no"])
        print("Number of iterations done:", iterations)
        break
    iterations += 1
