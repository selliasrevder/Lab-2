import random
from csv import reader


doc=open("3task.txt", "w")


count = 0
nomer = 0
random_array = [random.randint(1, 9410) for _ in range(20)]

with open('books-en.csv', 'r') as list:
    file = reader(list, delimiter=';')
    for row in file:
        count+=1
        if count in random_array:
            nomer += 1
            doc.write( f"{nomer}. {row[2]}. {row[1]} - {row[3]}" + '\n')

doc.close()
            
            

if __name__ == "__main__":
    print('List has been generated')