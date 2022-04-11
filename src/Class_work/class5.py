"""
def main():
    val1 = 3
    val2 = 4
    total = sum(val1, val2)
    print('The total value is:', total)

def sum(num1, num2):
    result = num1 + num2
    return result

main()
"""
"""
DISCOUNT_PERCENTAGE = 0.20

def main():

    reg_price = get_regular_price()

    sale_price = reg_price - reg_price * discount(reg_price)

    print('The sale price is $', format(sale_price, ',.2f'))

def get_regular_price():
    price = float(input('Please enter the regular price'))
    return price 

def discount(price):
    return price * DISCOUNT_PERCENTAGE
main()
"""

number = int(input('Enter a number: '))
if is_even(number): 
    print('The number is even.')
else:
    print('The number is odd.')

def is_even(num):
    if(num % 2) == 0:
        status = True
    else: 
        status = False 
    return status