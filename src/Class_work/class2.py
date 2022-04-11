""""
def main():
    value = 5
    show_double(value)

    show_double(num)

def show_double(x):
    result = x * 2
    print('The result is: ', result)

#call the main function
main()
"""

#This program demostrates a function that accepts two arguments

"""
def main():
   print('the sum of 12 and 45 is: ')
   show_sum(12, 45)

def show_sum(num1, num2):
    result = num1 + num2
    print(result)

main() 
"""

def main():
    value = 99
    print('The values is', value)
    change_me(value)
    print('Backin main the value is', value)

def change_me(arg):
    print('I am changing the value. ')
    arg = 0
    print('Now the value is', arg)

main()