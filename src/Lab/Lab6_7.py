"""
Design a program that generates a seven-digit number. The program should generate
seven random numbers, each in the range of 0 through 9.
"""
# import the random module
import random


# define the main function
def main():

    # ask the player to choose random numbers between 0 and 9:
    print("Choose 7 numbers between 0 and 9: ")
    # call the function which does it
    user_choices()

    # call random generator:
    random_number_list = random_generator()

    # display the numbers:
    display_numbers(random_number_list)


# create a random generator function
def random_generator():
    """
    :return: a list filled with 7 random integers
    """

    # create an empty list and fill it with random numbers
    random_numbers = []
    for number in range(1, 8):
        number = random.randint(0, 9)
        random_numbers.append(number)

    return random_numbers


# create a function which displays the random generated lists
def display_numbers(random_numbers):

    index = 1
    for random_number in random_numbers:
        print(f"The number {index} is {random_number}")
        index += 1


# create a function which asks the player for 7 random numbers:
def user_choices():

    # loop through 7 numbers and ask the user for a value
    for i in range(1, 8):
        number = int(input(f"Insert choice number {i}: "))
        print(f"Number {i}: {number}")

    print("*"*13)

# call main function
main()