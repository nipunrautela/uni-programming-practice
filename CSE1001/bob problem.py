n = float(input("Enter amount in hand: "))
c = float(input("Enter price of one chocolate: "))
m = float(input("Enter number of wrapper for free chocolate: "))

# compute number of chocolates bought
p = n//c
# compute number of free chocolates
f = p//m

print("Number of chocolates: ", int(p+f))
