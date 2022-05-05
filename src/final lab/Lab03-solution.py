# Solutions of Lab03

### Assignment 1
##keep_going = 'y'
##
##while keep_going == 'y':
##    number1 = float(input('Please enter a number: '))
##    number2 = float(input('Please enter another number: '))
##    result = number1 + number2
##    print('The result is: ', result)
##    keep_going = input('Do you want to add two more numbers? enter y for yes: ')
    
    

### Assignment 2
##total = 0
##
##print('This program gets 10 numbers from the user and'
##      + ' displays the total.')
##for i in range(10):
##    number = float(input('Please enter a number: '))
##    total += number
##
##print('The total is:', total)




#### Assignment 3
##total = 0
##for number in range(100, 0, -2):
##    if number > 2:
##        print(number, end = ', ')
##    else:
##        print(number)
##        
##    total += number
##
##print('The total of 100 + 98 + ... + 2 is: ', total)





### Assignment 4
##number = float(input('Please enter a positive nonzero number: '))
##while number <= 0:
##    print('Your answer is NOT a valid number.')
##    number = float(input('Please enter a positive nonzero number: '))
##
##print('Your answer is a valid number.')





   
### Assignment 5
##number = float(input('Please enter a number in the range of 1 through 100: '))
##while number < 1 or number > 100:
##    print('Your answer is NOT a valid number.')
##    number = float(input('Please enter a number in the range of 1 through 100: '))
##
##print('Your answer is a valid number.')







### Assignment 6	
##total = 0
##
##print('This program keeps a running total of the number of' 
##      + ' bugs collected during the five days.')
##
##for i in range(5):
##    number = int(input('Please enter the number of bugs you collected today: '))
##    total += number
##
##print('The total number of bugs collected is', total, 'bugs.')








