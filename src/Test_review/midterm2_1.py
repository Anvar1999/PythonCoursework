# Answer to the question 1


# write a function that accepts a list and the indexes of two elements in the list,
# and swaps that two elements of the list, and return the swapped list. 
# for example, if the arguments of the function are [23,65,19,90]m index1 = 1, and index2 = 3,
# then it will return [23,90,19,65].



# Python3 program to swap elements
# at given positions
    
# Swap function

def swapPositions(list, pos1, pos2):

     

    # popping both the elements from list

    first_ele = list.pop(pos1)   

    second_ele = list.pop(pos2-1)

    

    # inserting in each others positions

    list.insert(pos1, second_ele)  

    list.insert(pos2, first_ele)  

     

    return list
 
# Driver function

List = [23, 65, 19, 90]

pos1 = int(input('Enter the pos1'))
pos2 = int(input('Enter the pos2'))
 

print(swapPositions(List, pos1-1, pos2-1))