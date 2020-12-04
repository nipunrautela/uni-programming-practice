d = int(input("Enter the number to check divisibility by: "))
n = int(input("Enter a number: "))
while(n%d != 0):
    n = int(input("Enter a number: "))
print(f"{n} is divisible by 3")