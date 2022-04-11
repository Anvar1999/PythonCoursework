#Write a while loop that asks the user to enter two numbers. 
#The numbers should be added, and the sum displayed. 
#The loop should ask the user if he or she wishes to perform the operation again.
#If so, the loop should repeat, otherwise it should terminate.

continue_1 = 'y'
while continue_1 == 'y':
    number_1 = int(input('please enter your 1st number '))
    number_2 = int(input('please enter your 2nd number '))

    sum = number_1 + number_2
    print('Sum of two numbers are', sum)

    continue_1 = input("Do you want to continue; y for yes, n for no")