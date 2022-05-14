from array import *

# grades = [[45,37,54],[62,58,59],[79,47,60],[78,83,62]]
# print(grades)

# grades = [{'MA':45,'En':37,'Fr':54},{'MA':62,'En':58,'Fr':59},{'MA':79,'En':47,'Fr':60},{'MA':78,'En':83,'Fr':62}]
# print(grades[0]["En"])

# grades = {"Susan":{'MA':45,'En':37,'Fr':54},"Peter":{'MA':62,'En':58,'Fr':59},"Far":{'MA':79,'En':47,'Fr':60},"Car":{'MA':78,'En':83,'Fr':62}}
# print(grades)



# simple_array = [[2,5,8],[3,7,4],[1,6,9]]
# for x in simple_array:
#     print(x)

# print(simple_array[1])

# simple_array[2][1] = 5
# print(simple_array)
# print(simple_array[1][2])
# simple_array[1].append(3)
# print(simple_array)

# data_set = {'A':{'x': 54, 'y': 82, 'z':91}, 'B':{'x':75,'y':29,'z':80}}
# print(data_set)

# print(data_set['A'])
# print(data_set['B']['x'])
# print(data_set["A"])
# for i in data_set:
#     print(data_set[i]['y'])
# data_set["B"]['y'] = 53
# print(data_set["B"]['y'])




# indexing = [[2,3,4],[3,7,4],[1,6,9],[4,2,0]]
# for i in indexing:   
#     print(i)
    
# raw = int(input("Select a row"))
# column = int(input("Select a column"))

# print(indexing[raw][column])




# indexing = [[2,3,4],[4,5,6],[6,7,8],[3,6,7]]
# for i in indexing:
#     print(i)

# raw = int(input('Which raw would you like to be displayed: '))

# print(indexing[raw])

# new_value = int(input("Enter new value: "))
# indexing[raw].append(new_value)
# print(indexing[raw])





# indexing = [[1,2,3],[2,4,5],[2,4,1],[2,2,2]]
# for x in indexing:
#     print(x)

# raw = int(input('Which raw do you want be displayed: '))
# print(indexing[raw])
# column = int(input("Which collumn you want be displayed in this raw: "))
# print(indexing[raw][column])

# want = 'yes'

# while want == 'yes':
#     ask = input("Do you want to change the value? yes or no")
#     if ask == 'yes':
#         new_value = int(input("Whats the new value: "))
#         indexing[raw][column] = new_value
#         want = 'no'
#     else:
#         print("Have a good day!")
#         want = 'no'

# for x in indexing:
#     print(x)



# dct = {'John':{'N' : 3056,'S' :8463,'E' : 8441,'W' : 2694},'Tom':{'N' : 4832,'S' :6786,'E' : 4737,'W' : 4737},'Anne':{'N' : 5239,'S' :4802,'E' : 5820,'W' : 1859},'Fiona':{'N' : 3904,'S' :3645,'E' : 8821,'W' : 2451}}

   
# name = input("Enter the name: ")
# region = input("enter the region: ")

# print(dct[name][region])

# new_value = int(input("Enter new values: "))
# dct[name][region] = new_value
# print(dct[name])



    
# dct = {}
# for i in range(3):
#     name = (input('enter your name: '))
#     age = int(input('enter your age: '))
#     shoe_size = int(input("enter your shoe size: "))
#     dct[name] = {"Age":age,"Shoe size":shoe_size}
# enter = input("Who you want display: ")
# print(dct[enter])

# for name in dct:
#     print((name),dct[name]["Age"])



# dct = {}
# for i in range(3):
#     name = (input('enter your name: '))
#     age = int(input('enter your age: '))
#     shoe_size = int(input("enter your shoe size: "))
#     dct[name] = {"Age":age,"Shoe size":shoe_size}
# print(dct)
# enter = input("Who you want remove: ")
# print(dct[enter])

# del dct[enter]
# print(dct)


# for name in dct:
#     print((name),dct[name]['Age'], dct[name]['Shoe size'])




 