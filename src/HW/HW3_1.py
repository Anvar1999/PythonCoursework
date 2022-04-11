#Write a program that asks the user to enter the amount that he or she has budgeted for a month.
#A loop should then prompt the user to enter each of his or her expenses for the month and 
#keep a running total (user enters 0 to mark the end of her expenses).
#When the loop finishes, the program should display the amount that the user is over or under budget. 


#For me the vague part of the question was, 'over or under budget': Is the under budget means less than 0? and over budget means more than 0? if yes, then its fine.
budget = int(input("Enter your budgeted amount for a month: "))
continue_1 = 'y'
while continue_1 == 'y' and continue_1 != '0':
    expence = int(input('Enter your expence '))
    budget -= expence 
    continue_1 = input('Do you want add more expence? then type y for yes, and 0 for no ')

if budget > 0:
    print('Over budget $%.d' % budget)
else:
    print('Under budget $%.d' % budget)
