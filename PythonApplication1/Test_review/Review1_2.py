##Write a program that asks how long it took to run 10 km today. The program continues to ask how long (in minutes) it took for additional runs, 
##until the user enters 0. At that point, the program calculates and displays the average time that the 10 km run took.

i = 0
sum_run = 0
run = None
while run != 0:
    run = int(input('How long it took to run 10 km today? '))
    i += 1
    sum_run += run 

average_time = sum_run / i 
print('average sum %f over %d runs' %(average_time, i))