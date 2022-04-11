# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
# The program should first ask for the number of years. The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.
# Each iteration of the inner loop will ask the user for the inches of rainfall for that month.
# After all iterations, the program should display the number of months, the total inches of rainfall,
# and the average rainfall per month for the entire period. 

#Defining the variable total
total = 0

#asks the user to input the number of years
years = int(input("Enter the number of years: "))

#this loop uses the number taken from input to variable years. And calculates the total and inches for each month, each time it iterates. 
for y in range(years):
    for m in range(12):
        inches = int(input("How many inches fall for each month: "))
        total += inches

#this code calculates the average rainfall for each months. And gets the proper number of months
average = total/12 
months = years * 12

#Prints the whole number of months, total and average rainfall for each months. 
print("Number of months", months)
print("The total inches of rainfall", total)
print("The average rainfall per month for the entire period", average)
