fo = open("./CSE1001/storage/foo.txt", "w")

fo.write("Hello! Welcome to Python Files.")

print("File Name: ", fo.name)
print("Is Closed? ", fo.closed)
print("File Mode: ", fo.mode)

fo.close()
print(fo.closed)

fo = open("./CSE1001/storage/foo.txt", "r")
print(fo.read())
fo.close()
