import csv
from turtle import title



# file = open("Stars.csv","w")
# newRecord = "Brian, 23, Taurus\n"
# file.write(str(newRecord))
# file.close()




# file = open("Stars.csv","a")
# name = input("Enter name: ")
# age = input("Enter age: ")
# star = input("Enter star sign: ")
# newRecord = name + "," + age + "," + star + '\n'
# file.write(str(newRecord))
# file.close()



# file = open("Stars.csv","r")
# for row in file: 
#     print(row)


# file = open("stars.csv","r")
# reader = csv.reader(file)
# rows = list(reader)
# print(rows[1])



# file = open("Stars.csv","r")
# search = input("Enter the data you are searching for: ")
# reader = csv.reader(file)
# for row in file:
#     if search in str(row):
#         print(row)



# file = list(csv.reader(open("Stars.csv")))
# tmp = []
# for row in file:
#     tmp.append(row)


# file = open("NewStars.csv",'w')
# x = 0
# for row in tmp:
#     newRec = tmp[x][0] + ',' + tmp[x][0] + "," + tmp[x][2] + "\n"
#     file.write(newRec)
#     x = x + 1
# file.close()



# file = open("Books.csv",'w')
# content = "Book\t\t                                  Author            Year Released\n"
# a = "To kill A Mockingbird                         Harper Lee           1960\n"
# b = "A Brief History of Time                       Stephen Hawking      1988\n"
# c = "The Great Gatsby                              F. Scott Fitzgerald  1922\n"
# d = "The Man Who Mistock His Wife for a Hat        Oliver Sacks         1985\n"
# e = "Pride and Prejudice                           Jane Austen          1813\n"


# file.write(str(content))
# file.write(str(a))
# file.write(str(b))
# file.write(str(c))
# file.write(str(d))
# file.write(str(e))
# file.close()

# file = open("Books.csv", 'a')
# title_1 = input("Enter title data")
# Author =  input("Enter Author data")
# Year    = input("Enter Year data")
# newrecord = title_1 + ',' + Author + ',' + Year
# file.write(str(newrecord))
# file.close()

# file = open("Books.csv", 'r')
# for row in file:
#     print(row)
# file.close()




# file = open("Books.csv","r")
# lines = csv.reader(file)
# print(lines)
# file.close()
# file = open("Books.csv","a")
# print("How many do you want to add to the row ")
# add = int(input("add: "))
# for row in range(0,add):
#     Book = input("Enter the book: ")
#     Author = input("Enter the Author:")
#     YearReleased = input("Enter year: ")
#     newRec = Book + ',          ' + Author + ',         ' + YearReleased + '\n'
#     file.write(str(newRec))

# file.close()

# searchauthour = input("Enter the author you looking for: ")
# file = open("Books.csv","r")
# count = 0
# for row in file:
#     if searchauthour in str(row):
#         print(row)
#         count = count + 1 
# if count == 0:
#     print("There are no books by that author in that list. ")
# file.close()



start = int(input("Enter starting year: "))
end =  int(input("Enter ending year: "))
file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int (tmp[x][2]) <= end:
        print(tmp[x])
        x = x + 1 

    
