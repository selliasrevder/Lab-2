from csv import reader

with open('books-en.csv', 'r') as list:
    file = reader(list, delimiter=';')
    author_name=input("Author's name: ")
    books = []
    for row in file:
        if row[2] == author_name and int(row[3]) >= 2000:
            books.append(row[1])

    if books:
        for book in books:
            print(book)
    else:
        print("No books after 2000")