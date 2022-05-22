
# def get_name():
#     user_name = input("Enter your name: ")
#     return user_name

# def print_Msg(user_name):
#     print("Hello", user_name)

# def main():
#     user_name = get_name()
#     print_Msg(user_name)

# main()



# def get_data():
#     user_name = input("Enter your name: ")
#     user_age = int(input("Enter your age: "))
#     data_tuple = (user_name, user_age)
#     return data_tuple 

# def message(user_name, user_age):
#     if user_age <= 10:
#         print("Hi", user_name)
#     else:
#         print("Hello",user_name)

# def main():
#     user_name,user_age = get_data()
#     message(user_name,user_age)
# main()



# def enter_number():
#     num = int(input("Enter a number: "))
#     return num

# def another_program(num):
#     count = 0
#     while count != num:
#         count = count + 1
#         print("count: ", count)

# def main():
#     num = enter_number()
#     another_program(num)

# main()




# import random

# def values():
#     pick_low = int(input("Enter a low number: "))
#     pick_high = int(input("Enter a high number: "))
#     comp_num = random.randrange(pick_low,pick_high)
#     return comp_num

# def instructions():
#     guess = int(input("I'm thinking of a number: "))
#     return guess

# def third(comp_num, guess):
#     try_again = True
#     while try_again == True:
#         if guess == comp_num:
#             print("Correct")
#             try_again = False
#         elif guess > comp_num:
#             guess = int(input("Too high, enter another: "))
#         else: 
#             guess = int(input("Too low, enter another: "))


# def main():
#     comp_num = values()
#     guess = instructions()
#     third(comp_num, guess)
# main()


# import random
# from tkinter.font import names


# def subprogram_1():
#     generate1 = random.randrange(5,20)
#     generate2 = random.randrange(5,20)
#     correct_answer = generate1 + generate2
#     print(generate1,"+",generate2,"=", end = ' ')
#     ask_user = int(input())
#     answer = (correct_answer,ask_user)
#     return answer

# def subprogram_2():
#     num1 = random.randrange(25,50)
#     num2 = random.randrange(25,50)
#     correct_answer = num1 - num2 
#     print(num1,"-",num2,"=",end = " ")
#     ask_user = int(input())
#     answer = (correct_answer,ask_user)
#     return answer
# def check(correct_answer,ask_user):
#     if correct_answer == ask_user:
#         print("correct")
#     else:
#         print("Incorrect: the correct answer is ", correct_answer)


# def main():
#     print("1) Addition")
#     print("2) Subtraction")
#     enter = int(input("Enter 1 or 2: "))
#     if enter == 1:

#         correct_answer,ask_user = subprogram_1()
#         check(correct_answer,ask_user)
#     elif enter == 2:
#         correct_answer,ask_user = subprogram_2()
#         check(correct_answer,ask_user)
#     else: 
#         print("Incorrect choice: ")

# main()




# def add_name():
#     name = input("Enter name: ")
#     names.append(name)
#     return names

# def change_name():
#     num = 0 
#     for x in names:
#         print(num,x)
#         num = num + 1
#     select_name = input("Select a name to change: ")
#     name = input("Enter a new name: ")
#     names[select_name] = name
#     return names
# def delete_name():
#     num = 0 
#     for x in names:
#         print(num,x)
#         num = num + 1
#     select_num = int(input("Select a num to delete: "))
#     del names[select_num]
#     return names
# def view_names():
#     for x in names:
#         print(x)
#     print()
# def main():
#     again = 'y'
#     while again == 'y':
#         print("Menu: \nOption1: Add a name\nOption2: Change a name\nOption3: delete_name\nOption4: View all names\nOption5: End the program")
#         selectoption = int(input("Enter the option you like: "))
#         if selectoption == 1:
#             names = add_name()
#         elif selectoption == 2:
#             names = change_name()
#         elif selectoption == 3:
#             names = delete_name()
#         elif selectoption == 4:
#             names = view_names()
#         elif selectoption == 5:
#             again = 'n'       
#         else:
#             print("Wrong option ")
#         data = (names,again) 
# names = []   
# main()



# import csv

# def add_file():
#     file = open("Salaries.csv", "a")
#     name = input("Enter your name: ")
#     Salary = int(input("Enter your salary: "))
#     newrecord = name + ',' + str(Salary) + '\n'
#     file.write(str(newrecord))
#     file.close()

# def records():
#     file = open("Salaries.csv","r")
#     for row in file:
#         print(row)
#     file.close()
# def deleteRec():
    
#     file = csv.reader(open("Salaries.csv"))
#     x = 0
#     tmp = []
#     for row in file:
#         tmp.append(row)
#     file.close()
#     for row in tmp:
#         print(x,row)
#         x = x + 1
#     rowtodel = int(input("enter a row to delete: "))
#     del tmp[rowtodel]
#     file = open("Salaries.csv","w")
#     for row in tmp:
#         file.write(row)
#     file.close()

# again = 'y'
# while again == 'y':
#     print("1) Add to file")
#     print("2) View all records")
#     print("3) Delete a record")
#     print("4) Quit program")
#     print()
#     selection = int(input("enter a number of selection"))
#     if selection == 1: 
#         add_file()
#     elif selection == 2:
#         records()
#     elif selection == 3:
#         deleteRec()
#     elif selection == 4:
#         again = 'n'
#     else:
#         print("Wrong choice")