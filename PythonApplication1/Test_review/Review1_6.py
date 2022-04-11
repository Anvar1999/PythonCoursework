### P #6
##
### main function
##def main():
##    
##    # Local variable
##    number = 0
##
##    # Get number
##    number = int(input('Enter an integer: '))
##
##    # display information regarding whether the number is prime
##    if is_prime(number):
##        print ('The number you entered is a prime number.')
##    else:
##        print ('The number you entered is not a prime number.')
##
### The is_prime function receives a number as an argument,
### and returns True if number is prime, False otherwise. 
##def is_prime(number):
##    status = True
##    
##    for count in range(2, number):
##        if number % count == 0:
##            status = False
##        
##    return status
##    
##
### Call the main function.
##main()