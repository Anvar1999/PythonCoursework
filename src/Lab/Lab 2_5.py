##Write a program that asks the user to enter a number. If the number is divisible by 4, displays ‘The 
##number is divisible by 4’ and displays the quotient of the division. If the number is not divisible by 4, 
##displays ‘The number is not divisible by 4’ and displays the quotient and the remainder of the division.

number = int(input("Please enter a number: "))

if number % 4 == 0: 
    print("Number is divisable by 4")
else:
    print("Number is not divisable by 4")