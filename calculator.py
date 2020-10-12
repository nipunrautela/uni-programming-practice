while True:
    print("What action do you want to perform?\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Quit\n")
    action = int(input("Your choice: "))
    if action == 5:
        print("Exiting now...")
        break
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    if action == 1:
        print("Sum:", round(a+b, 2))
    elif action == 2:
        print("Difference:", round(a-b, 2))
    elif action == 3:
        print("Product:", round(a*b, 2))
    elif action == 4:
        print("Quotient:", round(a/b, 2))
    else:
        print("Invalid operation")
    input()
    