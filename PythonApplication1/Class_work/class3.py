"""
def main():
    print('I have a message for you. ')
    message()
    print('Goodbye! ')


def message():
    print('I am Arthur,')
    print('King of the Britons.')
main()  ## I called main function, because without main() it main method wouldn't work
"""

"""
def main():
    get_name()
    

def get_name():
    name = input('Enter your name: ') ## local variables can be accessed only inside the function,
    print('Hello', name)
main()
"""

## Argument

##function_name(argument)

"""
def function_name(parameter):
    statement
    statement 
    etc.
"""
def main():
    value =5
    show_double(value)    ## variable value jumps to argument number   10
    show_double(10)         ## 20
    num = 50
    show_double(num)


def show_double(number):
    result = number * 2
    print(result) 
main()
