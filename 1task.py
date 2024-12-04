from csv import reader

count = 0

with open('books-en.csv', 'r') as list:
    file = reader(list, delimiter=';')
    for row in file:
        if len(row[1]) > 30:
            count += 1

    print(count)    

    
