from array import *
import random
import math
# nums = array('i',[45,324,654,45,264])
# print(nums)

# for x in nums:
#     print(x)

# newValue = int(input("Enter number: "))
# nums.append(newValue)
# print(nums)
# nums.reverse()
# print(nums)
# nums = sorted(nums)
# print(nums)
# nums.pop()
# print(nums)

# newArray = array('i',[])

# more = int(input("How many items: "))
# for y in range(0,more):
#     newValue = int(input("Enter num: "))
#     newArray.append(newValue)
# print(newArray)
# nums.extend(newArray)
# print(newArray)


# getRid = int(input("Enter item index: "))
# nums.remove(getRid)

# print(nums.count(45))



# lst1 = array('i',[])
# for x in range(0,5):
#     lst = int(input("Enter a list of five integers: "))
   
#     lst1.append(lst)
# lst1 = sorted(lst1)
# lst1.reverse()
# print(lst1)




# nums = array('i', []) 
# for i in range(0,5):

#     num = random.randint(1,100)
#     nums.append(num)
#     print(num)




# arr = array('i',[])

# for i in range(0,5):
#     numbers = int(input("Enter numbers: "))
#     if numbers > 10 and numbers < 20:
#         arr.append(numbers)
#     else:
#         print("the %.0f Outside of the range" % numbers)

# print("Thank you")

# for i in arr:
#     print(i)




# arr = array('i',[1,2,3,3,4])
# print(arr)
# enter = int(input("enter one of the numbers in the array: "))
# times = arr.count(enter)
# print(times,'times appeared in the list: ')




# arr1 = array('i',[])
# arr2 = array('i',[])

# for i in range(0,3):
#     enter = int(input("Input numbers: "))
#     arr1.append(enter)

# for i in range(0,5):
#     j = random.randint(1,100)
#     arr2.append(j)

# print(arr1)
# print(arr2)
# arr1.extend(arr2)
# arr1 = sorted(arr1)
# print(arr1)
# for x in arr1:
#     print(x)





# arr = array('i',[])
# for i in range(0,5):
#     five = int(input("Enter numbers: "))
#     arr.append(five)
# arr = sorted(arr)
# print(arr)
# select = int(input("select one: "))
# arr.remove(select)
# print(select, "is removed from the list")
# print(arr)




# arr = array('i',[1,2,3,4,5])
# print(arr)
# try:
#     select = arr.index(int(input("Select one of the array numbers: ")))
#     print("Its position in array is", select)
# except:
#     print("This is not in the array: ")


arr = array('f',[15.00,16.00,17.00,18.00,19.00])
whole = int(input("Enter numbers between 2  and 5: "))
i = True
while i == True:
    
    if whole < 5 and whole > 2: 
        print("Thank you: ")
        i = False
        
    else:
        print("Try again, enter suitable number: ")
        whole = int(input("Enter numbers between 2  and 5: "))
    
    
for x in arr:
    j = x / whole
    print(round(j,2))




