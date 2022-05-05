# Solutions of Lab04

### Assignment 1

##number = float(input('Please enter a number in the range of 1 through 100: '))
##while number < 1 or number > 100:
##    print('Your answer is NOT a valid number.')
##    number = float(input('Please enter a number in the range of 1 through 100: '))
##
##print('Your answer is a valid number.')
    
    

### Assignment 2

### There are 7 rows in the pattern, so we use range(7)
##for row in range(7):
##    # Because the number of '#' in each row is (7 - row)
##    # we should iterate (7 - row) times
##    for col in range(7 - row):
##        print('#', end = '')
##    # Use print() function to jump to the next line
##    print()




#### Assignment 3

### the function name is show_value, and the argument should be 12
### Call show_value function
##show_value(12)




### Assignment 4

##def times_ten(number):
##    result = number * 10
##    print('The result is:', result)
##
### Call the times_ten function and pass 5 as argument
##times_ten(5)




   


### Assignment 5

### the main function
##def main():
##
##    # Get the distance in kilometers from user
##    distance = float(input('Please enter a distance in kilometers:'))
##
##    # call the show_miles function
##    show_miles(distance)
##    
##
### the show_miles function
##def show_miles(kilometers):
##
##    # Calculate the distance in miles
##    miles = kilometers * 0.6214
##
##    # Display the distance in miles
##    print('The distance in miles is:', format(miles, ',.2f'), 'miles.')
##    
##
### Call the main function
##main()
    








