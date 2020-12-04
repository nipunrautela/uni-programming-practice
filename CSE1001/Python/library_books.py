n = int(input("Enter the number of books: "))

bookid = []
book_name = []
author = []
publisher = []
year_of_p = []
pages = []
cost = []
copies = []

for i in range(n):
    print("Enter the info for Book", i+1, "\b:-")
    bookid.append(input("Book Id: "))
    book_name.append(input("Book Name: "))
    author.append(input("Author name: "))
    publisher.append(input("Publisher: "))
    year_of_p.append(int(input("Year of Publication: ")))
    pages.append(int(input("Number of pages: ")))
    cost.append(int(input("Cost: ")))
    copies.append(int(input("Copies available: ")))

search = input("Enter the book id you want to search")
ye = 0
for i in range(n):
    if bookid[i] == search:
        print(bookid[i])
        print(book_name[i])
        print(author[i])
        print(publisher[i])
        print(year_of_p[i])
        print(pages[i])
        print(cost[i])
        print(copies[i])
        ye = 1
if ye == 0:
    print(search, "not found")