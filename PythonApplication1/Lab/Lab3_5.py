#Write code that prompts the user to enter a number in the range of 1 through 100 and validates the input.

number = int(input('Please enter a number '))
if number >= 1 and number <= 100:
    print("Your input is ", number)
else:
    print('Wrong input ')