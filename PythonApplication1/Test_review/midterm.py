#code 1
#even and odd
#shut down on negative number
"""
even_sum = 0
odd_sum = 0
def is_even(num):
   if(num % 2) == 0:
        status = True
   else:
        status = False
   return status 
number = int(input("Enter a number: "))
while number >= 0:


    
    if is_even(number):
         even_sum = even_sum + number 
    else:
        odd_sum = odd_sum + number
    number = int(input('Enter a number: '))


print('even sum = ', even_sum)
print('odd sum = ', odd_sum)
"""


"""
#code2
Celsius_1 = int(input("Enter the first  temperature in Celcius "))
Celsius_2 = int(input("Enter the second temperature in Celcius "))


if Celsius_1 < Celsius_2:
    min_temp = Celsius_1
    max_temp = Celsius_2
else:
    min_temp = Celsius_2
    max_temp = Celsius_1


F_1 = (9/5)*max_temp +32

while min_temp < max_temp:
    F = (9/5)*min_temp +32
    print("C %d degree" % min_temp, "F %d degree" % F)
    min_temp += 1


print("C %d degree" % max_temp, "F %d degree" % F_1)
 """   

 """
even_sum = 0
odd_sum = 0

number = int(input("Enter a number: "))
while number >= 0:


    
    if number % 2 == 0:
         even_sum += number 
    else:
        odd_sum += number
    number = int(input('Enter a number: '))


print('even sum = ', even_sum)
print('odd  sum = ', odd_sum)
"""

