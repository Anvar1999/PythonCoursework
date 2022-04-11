## 1. Write Python code that prompts the user to
## enter a number and assigns the user input to variable
## speed. Then. 
## a. write an if statement that displays the message 
## "The number is valid" if the value referenced speed is within
## the range 0 through 200.
## b. Write an if statement that displays the message "The number is not valid"
## if the value referenced by speed is outside the range 0 through 200.

speed = int(input("Please enter the number: "))
if speed >= 0 and speed <= 200:
    print("The number is valid")
else:
    print("The number is not valid")