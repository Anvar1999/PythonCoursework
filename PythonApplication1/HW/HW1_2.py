##2. Write a program that converts Celsius temperatures to Fahrenheit temperatures. The 
##formula is as follows: 
##F = 9/5 C + 32
##The program should ask the user to enter a temperature in Celsius, then display the 
##temperature converted to Fahrenheit. [50 points]

##The formula will be Fahrenheit = (Celsius * 9/5) + 32

Celsius = float(input("Converter: Please enter the temperature in Celsius and get the answer in Fahrenheit: "))
Fahrenheit = (Celsius * 9/5) + 32
print('Convertion complete: its %0.2f Fahrenheit' %(Fahrenheit))



