#A bug collector collects bugs every day for 5 days.
#Write a program that keeps a running total of the number of bugs collected during the five days. 
#The loop should ask for the number of bugs collected for each day, and when the loop is finished, 
#the program should display the total number of bugs collected. 
i = 0
summary = 0
while i < 5:

    bugs = int(input("How many bugs you collected today? "))
    summary = summary + bugs
    i = i + 1
print('Total bugs numbers in 5 days is ', summary)
