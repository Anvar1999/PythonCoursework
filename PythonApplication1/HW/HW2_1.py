
## This printline is used to display choices in menu
print('choose primary color to mix \n1.blue \n2.yellow \n3.red')

## I used while operater to continue the program
continue_choice = 'y'
while continue_choice == 'y':
   
## These two input line is used for to take the choice input from the user 
    choice_1 = input('Choose your first color:  ')
    choice_2 = input('Choose your second color: ')

## Basic if else statement is used for to mix choices and get answers
    if choice_1 == 'blue' and choice_2 == 'yellow':
        print('green')
    elif choice_1 == 'yellow' and choice_2 == 'blue':
        print('green')
    elif choice_1 == 'red' and choice_2 == 'yellow':
        print('orange')
    elif choice_1 == 'yellow' and choice_2 == 'red':
        print('orange')
    elif choice_1 == 'red' and choice_2 == 'blue':
        print('purple')
    elif choice_1 == 'blue' and choice_2 == 'red':
        print('purple')
    else:
        print('Wrong input')

## Preventing the error from wrong input 
    if choice_1 == 'blue' and choice_2 == 'blue':
        print('You cannot mix same color')
    elif choice_1 == 'yellow' and choice_2 == 'yellow':
        print('You cannot mix same color')
    elif choice_1 == 'red' and choice_2 == 'red':
        print('You cannot mix same color')

##To continue and to end the program I needed these 3 lines here
    continue_choice = input('Do you want to continue: \nChoose y for yes \nChoose n for no \nType your choice here: ')
    if continue_choice == 'n':
        print('Good bye!')