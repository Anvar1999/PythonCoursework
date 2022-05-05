# Solutions of Lab02
# Assignment 1
speed = int(input('Enter a number: '))
# part a
if speed >=0 and speed <=200:
    print('The number is valid.')
# part b
if speed < 0 or speed > 200:
    print('The number is not valid.')

# Assignment 2
a = 5
if a < 10:
    b = 0
else:
    b = 99


# Assignment 3
if score >= 90:
    print('Your grade is A.')
else:
    if score >= 80:
        print('Your grade is B.')
    else:
        if score >= 70:
            print('Your grade is C.')
        else:
            if score >= 60:
                print('Your grade is D.')
            else:
                print('Your grade is F.')


# Assignment 4
amount1 = 15
amount2 = 20
if amount1 > 10 and amount2 < 100:
    if amount1 > amount2:
        print (amount1)
    elif amount2 > amount1:
        print (amount2)
    else:
        print('Both values are the same.')


# Assignment 5
number = int(input('Please enter an integer number: '))
remainder = number % 4
quotient = number // 4
if remainder == 0:
    print('The number is divisible by 4.')
    print('The quotient is', quotient)
else:
    print('The number is NOT divisible by 4.')
    print('The quotient is', quotient,
          'and the remainder is', remainder)



# Assignment 6	
# Get the person's age.
age = int(input('Enter age: '))

# Determine if the person is an infant, child,
# teenager, or adult, and display the result.
if age <= 1:
    print('Infant')
elif age > 1 and age < 13:
    print('Child')
elif age > 13 and age < 20:
    print('Teenager')
else:
    print ('Adult')
