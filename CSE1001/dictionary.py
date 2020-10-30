contacts = {}
for i in range(5):
    relation = input("Enter the relation name: ")
    phno = int(input("Enter their Number"))
    
    contacts[relation] = phno

relation = input("Enter the relation to find number of: ")
print(contacts[relation] if relation in contacts else "No.")