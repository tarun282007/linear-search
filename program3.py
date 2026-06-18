# Book Library Search

books = ["Python Basics", "Data Structures", "Machine Learning",
         "Web Development", "Database Systems"]

search_book = input("Enter the book name to search: ")

found = False

for i in range(len(books)):
    if books[i].lower() == search_book.lower():
        print("Book found at index", i)
        found = True
        break

if not found:
    print("Book not found in the library")