import re
reg_no = input("Enter your register number: ")

if re.match("[1-9][0-9][A-Za-z]{3}[0-9]{4}", reg_no):
    print("Valid")
else:
    print("Invalid")