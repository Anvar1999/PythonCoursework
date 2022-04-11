#Write a loop that asks the user to enter a number.
#The loop should iterate 10 times and keep a running total of the numbers entered. 

count = 0
sum = 0
while count < 10:
    number = int(input('Please enter a number '))

  
    count = count + 1
    sum = sum + number

print(sum)