de = int(input("Enter the expected date of return"))
me = int(input("Enter the expected date of return"))
ye = int(input("Enter the expected date of return"))
da = int(input("Enter the actual date of return"))
ma = int(input("Enter the actual date of return"))
ya = int(input("Enter the actual date of return"))

if ye < ya:
    print("Fine:", 10000)
elif me <= ma:
    print("Fine:", (ma-me)*500)
elif de <= da:
    print("Fine:", (da-de)*15)
else:
    print("No fine.")