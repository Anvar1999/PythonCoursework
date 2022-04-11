"""
def is_even(num):
    if(num % 2) == 0:
        status = True
    else:
        status = False
    return status 

number = int(input('Enter a number: '))
if is_even(number):
    print('The number is even. ')
else:
    print('The number is odd. ')
"""
"""
def is_invalid(model_num):
    if model_num!= 100 and model_num!=200 and model_num!=300:
        status = True

    else:
        status = False
    return status 


model = int(input('Enter the model number' ))

while is_invalid(model):
    print('The valid model number are 100, 200, 300.')
    model = int(input('Enter a valid model number: ' ))
 """
"""
 #circle_area = math.pi * radius ** 2

 import math

 # The are func. accepts the radius of a circle and returns its area

 def area(radius):
     return math.pi * radius ** 2

 # The circumference func. accepts the radius of a circle and returns its circumference 

 def circumference(radius):
     return 2* math.pi * radius 
 """

 import circle 

 def main():

     radius = float(input('Please enter the radius of circles: '))

     circle_area = circle.area(radius)
     circle_circ = circle.circumference(radius)

     print('The area is:', format(circle_area, '.2f'))

     print('The circumference is: ', format(circle_circ, '.2f'))


main()

