n = int(input("Enter the number of students: "))
reg_no = []
name = []
subject1 = []
subject2 = []
subject3 = []
subject4 = []
total = []
average = []
result = []


for i in range(n):
    print("Enter Info for student", i+1, "\b:-")
    reg_no.append(input("Enter the register number: "))
    name.append(input("Enter the name: "))
    sub1 = int(input("Enter the subject 1 mark: "))
    sub2 = int(input("Enter the subject 2 mark: "))
    sub3 = int(input("Enter the subject 3 mark: "))
    sub4 = int(input("Enter the subject 4 mark: "))
    tot = sub1 + sub2 + sub3 + sub4
    avg = tot/4
    if (sub1>50) and (sub2>50) and (sub3>50) and (sub4>50):
        res = "PASS"
    else:
        res = "FAIL"
    
    subject1.append(sub1)
    subject2.append(sub2)
    subject3.append(sub3)
    subject4.append(sub4)
    total.append(tot)
    average.append(avg)
    result.append(res)

for i in range(n):
    print(name[i])
    print(reg_no[i])
    print(subject1[i])
    print(subject2[i])
    print(subject3[i])
    print(subject4[i])
    print(total[i])
    print(average[i])
    print(result[i])