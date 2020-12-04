n = int(input("Enter the number of students: "))
students = []

def passfail(marks):
    Pass = True
    for mark in marks:
        if mark < 50:
            Pass = False
    if Pass:
        return "PASS"
    else:
        return "FAIL"

def get_info():
    student = {}
    student['reg_no'] = input("Enter the register number: ")
    student['name'] = input("Enter the name: ")
    student['marks'] = [
        int(input("Enter the subject 1 mark: ")),
        int(input("Enter the subject 2 mark: ")),
        int(input("Enter the subject 3 mark: "))
    ]
    return student

for i in range(n):
    print("Enter Info for student", i+1, "\b:-")
    students.append(get_info())

for student in students:
    print('Name:', student['name'], '\n', 'Status:', passfail(student['marks']), '\n\n')
