


# countries_tuple = ("France","Germany","Poland","Russia","Ukraine")
# print(countries_tuple)
# ask = input("Enter one of the countries: ")
# print("Index of that country is ", countries_tuple.index(ask))

# enter_number = int(input("Enter the index of 5 countries: 0-4 "))
# print(countries_tuple[enter_number])



# lst = ["Taekwondo","Soccer"]
# print(lst)
# user = lst.append(input("What is your favourite sport? "))
# lst.sort()
# print(lst)


# lst = ["pen","pencil","book","notebook","laptop","eraser"]
# print(lst)
# dislike = lst.index(input("Which of these subjects you don't like"))
# del lst[dislike]
# print(lst)



# food_dictionary =  {}
# food1 = input("Enter a food you like: ")
# food_dictionary[1] = food1
# food2 = input("Enter other food: ")
# food_dictionary[2] = food2
# food3 = input("Enter another food: ")
# food_dictionary[3] = food3
# food4 = input("Enter one more food: ")
# food_dictionary[4] = food4 
# print(food_dictionary)
# getrid = int(input("Which of these food you want to get rid off: "))
# del food_dictionary[getrid]
# print(sorted(food_dictionary.values()))



# lst = ['red','blue','red','yellow','orange','green','white','black','pink','silver']
# start = int(input("Enter start number 0-4: "))
# end = int(input("Enter end number 5-9: "))
# print(lst[start:end])



# lst = [123, 321, 428, 324]
# for i in lst:
#     print(i)
# for i in lst:
#     try:
#         enter = lst.index(int(input("enter three digit number: ")))
#         print(enter)
#     except ValueError:
#         print("that is not in the list")





# lst = []
# for i in range(1,4):
#     name = input("Who do you want to invite: ")
#     lst.append(name)

# i = input("Do you want enter more names? enter yes or no: ")  
# while i != 'no':
    
#     name = input("Enter the name: ")
#     lst.append(name)
#     i = input("Do you want enter more names? enter yes or no: ")
    
# print("You have invited: %s" % lst)





# lst = []
# for i in range(1,4):
#     name = input("Who do you want to invite: ")
#     lst.append(name)

# i = input("Do you want enter more names? enter yes or no: ")  
# while i != 'no':
    
#     name = input("Enter the name: ")
#     lst.append(name)
#     i = input("Do you want enter more names? enter yes or no: ")
    
# print("You have invited: %s" % lst)
# ask = lst.index(input("Type in one of the name in the list"))
# print(ask,"position in the list")
# want = input("Do you still want that person to come: ")
# if want == 'no':
#     del lst[ask]
# print(lst)



# lst = ['Mtv','Ntv','Zortv','Tv']

# for i in lst:
#     print(i)

# new_lst = input("Do you want to enter more show: ")
# position = int(input("which position do you want to enter it: "))
# lst.insert(position , new_lst)
# print(lst)
# for i in lst:
#     print(i)




nums = []
num1 = int(input("Enter number 1: "))
nums.append(num1)
num2 = int(input("Enter number 2: "))
nums.append(num2)
num3 = int(input("Enter number 3: "))
nums.append(num3)
remove = input("Do you still want that last number to be entered: ")
if remove == 'no':
    nums.remove(num3)

print(nums)
