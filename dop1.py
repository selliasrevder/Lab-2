from csv import reader

with open('books-en.csv', 'r') as list:
    file = reader(list, delimiter=';')
    publisher = set(row[4] for row in file)
    for pub in publisher:
        print(pub)
    