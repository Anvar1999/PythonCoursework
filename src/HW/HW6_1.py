#Write a program that writes a series of random integer numbers to a file named random_numbers.txt.
# #Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold.
import random

afile = open("random_numbers.txt", "w" )
sum_num = 0
for i in range(1,500):
    line = int(random.randint(1, 500))
    sum_num = sum_num + line
    
    afile.write(str(line))
    print(str(line))
average = sum_num/500   
print('sum',sum_num)
print('500 random numbers read from the file')
print('average',average)
afile.close()

