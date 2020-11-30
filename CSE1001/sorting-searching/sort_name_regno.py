students = []
n = int(input("Enter the number of students: "))

for i in range(n):
    name = input("Enter name of student {}: ".format(i+1))
    regno = input("Enter reg no. of student {}: ".format(i+1))
    students.append([name, regno])

for i in range(len(students)):
    for j in range(i, len(students)):
        if students[i][1] > students[j][1]:
            temp = students[i]
            students[i] = students[j]
            students[j] = temp

for student in students:
    print(student[0])

'''
Test Case
11
Meghna Sinha
20BAI1133
Muhesh Kumar
20BAI1175
Subhadip Nandi
20BAI1131
Rohan Pawar
20BAI1200
Shreyes Ram V
20BAI1140
Divyashree Dev
20BAI1232
Nipun Rautela
20BAI1135
Varsha Sharma
20BAI1190
Aron Ritesh
20BAI1195
Jamal Mohammad Shakeel
20BAI1166
Indra Sigichalra
20BAI1107

'''
