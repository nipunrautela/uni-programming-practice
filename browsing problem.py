hours = int(input("Enter the number of hours browsed: "))
mins = int(input("Enter the number of minutes browsed: "))
amount = 0

if hours > 7 or (hours==7 and mins>0):
    print("You can not browse for more than 7 hours")
    exit()

amount += mins
while hours != 0:
    if hours >= 5:
        amount += 200
        hours -= 5
    elif hours > 0:
        amount += hours*50
        hours = 0
    
print("Amount to be paid: ", amount)
