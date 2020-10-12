while True:
    print("What action do you want to perform?\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit\n")
    action = int(input("Your choice: "))
    if action == 5:
        print("Exiting now...")
        break
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    if action == 1:
        print("Sum:", a+b)
    elif action == 2:
        print("Difference:", a-b)
    elif action == 3:
        print("Product:", a*b)
    elif action == 4:
        print("Quotient:", a/b)
    else:
        print("Invalid operation")
    input()
    