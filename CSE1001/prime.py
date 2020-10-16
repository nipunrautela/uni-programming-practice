a = []
n = int(input("Enter the amount of numbers: "))
for i in range(0, n):
    a.append(int(input("Enter number: ")))
    
for i in a:
    for j in range(2, int(i/2)):
        if i%j == 0:
            print(i, "is not prime.")
            break
    else:
        print(i, "is prime.")