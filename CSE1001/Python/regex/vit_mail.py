import re
reg_no = input("Enter your VIT mail: ")

if re.match("[a-z]+\.([a-z]+)?[1-2][0-9]{3}@vitstudent\.ac\.in$", reg_no):
    print("Valid")
else:
    print("Invalid")