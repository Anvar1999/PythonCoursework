"""
Write a function named max that accepts two integer values as arguments and returns the value that is the greater of the two.
For example, if 7 and 12 are passed as arguments to the function, the function should return 12. Use the function in a program 
that prompts the user to enter two integer values. The program should display the value that is the greater of the two. 
"""
number_1 = int(input("Enter the number 1: " ))
number_2 = int(input("Enter the number 2: " ))

def max(number_1,number_2):
    
    if number_1 > number_2:
        print(number_1)
    else:
        print(number_2)
        



max(number_1,number_2)
    