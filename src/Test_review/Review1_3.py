##Write a program that allows a user to keep inputting numbers until the number zero is entered. The program should keep track of 
#two separate sums: The sum of all positive numbers entered and the sum of all negative numbers entered. Once the loop ends the program 
#should display the two sums.

positive_sum = 0
negative_sum = 0
number = int(input("Please enter the number, enter 0 to end"))
while number != 0:

  
   if number > 0: 
    
    positive_sum = positive_sum + number 
   else:

    negative_sum = negative_sum + number
   number = int(input("Please enter the number, enter 0 to end"))


print('Positive sum = ', positive_sum)
print('Negative sum = ', negative_sum)