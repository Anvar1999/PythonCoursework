###Lab assignments # 7

### Assignment 1
### function that accepts a list as an argument
### and returns the total of the values in the list
##def total(List):
##    tot = 0
##    for item in List:
##        tot += item
##    return tot
##
##my_list = [1,2,3,4,5]
##print('The total of the values in', my_list, 'is', total(my_list))
    
    


#### Assignment 2

##names = ['Jack', 'Jill', 'John', 'Ruby']
##
##if 'Ruby' in names:
##    print('Hello Ruby')
##else:
##    print('No Ruby')





### Assignment 3
### function that accepts a list and swaps the
### first and the last element of the list
##def swapList(newList):
##    size = len(newList)
##     
##    # Swapping
##    temp = newList[0]
##    newList[0] = newList[size - 1]
##    newList[size - 1] = temp
##     
##    return newList
##
##my_list = [23, 65, 19, 90]
##print('The original list is:', my_list)
##print('After swapping first and last item:', swapList(my_list))





##### Assignment 4
### This function counts number of occurrences
### of x in the List
##def countX(List, x):
##    counter = 0
##    for item in List:
##        if item == x:
##            counter += 1
##
##    return counter
##
##my_list = [1, 3, 1, 3, 6, 3, 7, 8, 9, 3]
##print('The number of occurrences of', 3, 'in', my_list, 'is', countX(my_list, 3))






##### Assignment 5
### This function turn every item of the list into its square
##def squareList(List):
##    
##    sqList = []
##    
##    for item in List:
##        sqList.append(item ** 2)
##        
##    return sqList
##
##my_list = [1, 2, 3, 4]
##print('The square of numbers in', my_list, 'is', squareList(my_list))







##### Assignment 6
### This function find value 20 in a list,
### and if it is present, replace it with 200
##
##def findReplaceX(List, x):
##
##    newList = []
##        
##    for i in List:
##        if i == x:
##            newList.append(i * 10)
##        else:
##            newList.append(i)
##
##    return newList
##                 
##
##my_list = [10, 20, 30, 40, 20, 30]
##x = 20
##
##print('The original list is:', my_list)
##print('The modified list is:', findReplaceX(my_list, x))




#######Assignment 7
##
### The input list
##inputList = [1, 2, 2, 5, 8, 4, 4, 8]
##
### List for unique items 
##uniqueList = []
## 
### Counter for unique items
##count = 0
## 
### Traversing the list
##for item in inputList:
##    if item not in uniqueList:
##        count += 1
##        uniqueList.append(item)
## 
### Printing the output
##print("The original list is:", inputList)
##print("No. of unique items is:", count)
##print("The unique items are:", uniqueList)







###Assignment 8
# This function accepts a list of three items,
# and displays all possible combinations of them
##
##def combinations(List):
##      
##    for i in range(3):
##        for j in range(3):
##            for k in range(3):
##                  
##                # check if the indexes are not
##                # same
##                if (i!=j and j!=k and i!=k):
##                    print(List[i], List[j], List[k])
##
##L =  [0, 9, 5]                     
##print("The possible combinations of",L[0], L[1], L[2], "is:") 
##combinations(L)
##
##L =  ['one', 'two', 'three']                     
##print("The possible combinations of",L[0], L[1], L[2], "is:") 
##combinations(L)



