customer_info = []
customer_count = int(input("Enter the number of customers: "))

for i in range(customer_count):
    customer_info.append([
        input("Enter name of customer {0}: ".format(i+1)),
        int(input("Enter age of customer {0}: ".format(i+1))),
        input("Enter gender of customer {0}: ".format(i+1)),
        input("Enter region of customer {0}: ".format(i+1)),
    ])
region = input("Enter the region to check customers: ")
for customer in customer_info:
    if customer[3] == region:
        print("Customer Name:", customer[0])
        print("Customer Age:", customer[1])
        print("Customer Gender:", customer[2], end="\n\n")
# for input
# Nipun
# 18
# Male
# Delhi
# Someone
# 19
# Male
# Earth
# Another Person
# 34
# Female
# Delhi
# Kanika
# 23
# Female
# Noida
# Shras
# 18
# Male
# Chennai
# Muthun
# 18
# Male
# Chennai
