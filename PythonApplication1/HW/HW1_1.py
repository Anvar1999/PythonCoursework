##1. A customer in a store is purchasing five items. Write a program that asks for the price of 
##each item, then displays the subtotal of the sale, the amount of sales tax, and the total. 
##Assume the sales tax is 7 percent. [50 points]


laptop = int(input("What's the price of laptop? "))
mouse = int(input("What's the price of mouse? "))
headset = int(input("What's the price of headset? "))
table = int(input("What's the price of table? "))
GamingChair = int(input("What's the price of GamingChair? "))
total = (laptop + mouse + headset + table + GamingChair)
tax = total * 0.07
subtotal = tax + total
print('You entered 5 items: \nlaptop \t\t\t\t$%d \nmouse \t\t\t\t$%d \nheadset \t\t\t$%d \ntable \t\t\t\t$%d \nGamingChair \t\t\t$%d' %(laptop, mouse, headset, table, GamingChair))
print('Your all items costs:      \t$%d' % total)
print('The sales tax is 7 percent \t$%d' % tax)
print('Your subtotal:             \t$%d' % subtotal)