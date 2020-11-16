contacts = {}
# Input for contacts
# Human1
# 2463574672
# Human2
# 3546776871
# Human3
# 4253765785
# Human4
# 2435465769
# Human5
# 5364756762

for i in range(5):
    relation = input("Enter the relation name: ")
    phno = int(input("Enter their Number: "))
    
    contacts[relation] = phno

# For finding a number in relations
# relation = input("Enter the relation to find number of: ")
# print(contacts[relation] if relation in contacts else "No.")

# For finding even mobile numbers
# for key in contacts:
#     if contacts[key]%2 == 0:
#         print(contacts[key])
