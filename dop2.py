from csv import reader

with open('books-en.csv', 'r') as list:
    file = reader(list, delimiter=';')
    top_books = []
    for row in file:
        if row[5]!='Downloads':    
            book = row[1]
            author = row[2]
            popularity = int(row[5])
            top_books.append((popularity, book, author))

    top_books.sort(reverse=True)

    for i in range(20):
        print(f"{i + 1}.\t{top_books[i][2]} - {top_books[i][1]}")