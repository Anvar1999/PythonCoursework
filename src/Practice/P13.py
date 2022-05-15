import os
import json
# lst = [[1,2,3],[2,3,4],[3,4,5]]
# for i in lst:

#     for j in i:
#         print(j,end = " ")
#     print()




# file = open("Countries.txt","w")
# file.write("Italy\n")
# file.write("Germany\n")
# file.write("Spain\n")
# file.close()

# file = open("Countries.txt", 'r')
# print(file.read())

# file = open("Countries.txt",'a')
# file.write("France\n")
# file.close()

# file = open("Countries.txt",'r')
# print(file.read())


# file = open("Numbers.txt",'w')
# file.write('5,')
# file.write('5,')
# file.write('5,')
# file.write('5,')
# file.write('5')
# file.close()

# file = open("Numbers.txt",'r')
# print(file.read())




# file = open("Names.txt",'w')
# file.writelines(['Anvar','\n','Jo','\n','po','\n','so','\n','ho']) 

# file.close()

# file = open("Names.txt",'r')
# print(file.read())




# file = open('Names.txt','a')
# ask = input("Do you want to enter new name: ")
# file.write(ask)
# file.close()


# file = open('Names.txt','r')
# print(file.read())
# file.close()




# selection = int(input("Make a selection 1, 2 or 3: "))


# if selection == 1:
#     new_subject = input("enter a school subject: ")
#     file = open('Subject.txt','w')
#     file.write(new_subject + '\n')
#     file.close()
# elif selection == 2:
#     file = open('Subject.txt','r')
#     print(file.read())
#     file.close()
# elif selection == 3:
#     new_subject1 = input("enter a school subject: ")
#     file = open('Subject.txt','a')
#     file.write(new_subject1 + '\n')
#     file.close()
#     file = open('Subject.txt','r')
#     print(file.read())
    
# else:
#     print("Invalid selection")



"""
def increaseValue(line: str) -> str:
    valueStr = line.split(':')[1].strip().replace(",", "")
    value = int(valueStr) * 2
    line = line.replace(valueStr, str(value))
    return line

path = f"{os.getcwd()}\\src\\Practice\\sample.json"
file = open(path, "r+")
lines = file.readlines()

i = 0
for line in lines:
    widthIndex = line.strip().replace(" ", "").find("\"width\":")
    heightIndex = line.strip().replace(" ", "").find("\"height\":")

    if widthIndex != -1:
        lines[i] = increaseValue(line)

    if heightIndex != -1:
        lines[i] = increaseValue(line)

    i = i + 1
        
file.close()
file = open(path, "w")
file.writelines(lines)
file.close()
"""     




file = open('Names.txt','r')
print(file.readlines())
file.close()

file = open('Names.txt', 'r')
select = input("Enter the name to remove")
select = select + '\n'
for row in file:
    if row != select:
        file = open('Names2.txt', 'a')
        newrecord = row
        file.write(newrecord)
    file.close()
file.close()








