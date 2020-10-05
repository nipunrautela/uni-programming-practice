isFirstGrad = input("Are you first graduate? (yes/no)")
if isFirstGrad.lower() == "no":
    print("You're not eligible for scholarship.")
    exit()

phyMarks = int(input("Enter your Physics marks: "))
matMarks = int(input("Enter your Mathematics marks: "))
chyMarks = int(input("Enter your Chemistry marks: "))

if phyMarks >= 98 and matMarks >= 98 and chyMarks >= 98: 
    print("You're eligible for scholarship")
else:
    print("You're not eligible for scholarship.")