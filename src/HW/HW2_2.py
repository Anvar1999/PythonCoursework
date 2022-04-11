## 2. A software company sells a package that retails for $99. Quantity discounts are given according to the 
## following table. Write a program that asks the user to enter the number of
## packages purchased. The program should then display the amount of the discount (if any) and the total 
## amount of the purchase after the discount.


##Basic command line used for display the menu of the discounts and quantity
print('The cost of the package is $99: \nQuantity \tDiscount \n10-19 \t\t10% \n20-49 \t\t20% \n50-99 \t\t30% \n100 or more \t40%')

##Assigned value $99 to proper variable
company_package = 99

##Asks from the user to enter the quantity of package
quantity = int(input('Please enter the quantity of package: '))

##Basic math for calculating the total
total = quantity * company_package

##if else program used for calculate the proper total price, discount, and total after discount
if quantity >= 10 and quantity <= 19:
    after_discount = total - (total * .1)
    p = 10
elif company_package >= 20 and company_package <= 49:
    after_discount = total - (total * .2) 
    p = 20
elif company_package >= 50 and company_package <= 99:
    after_discount = total - (total * .3)
    p = 30
else:
    after_discount = total - (total * .4) 
    p = 40
discount = total - after_discount
##Command line used for display the total, discount, and total after discount
print('Total equals to \t\t$%0.2f' %(total) + '\nYou have %d%% discount' %(p) + '\t\t$%.2f' %discount)
print('After discount total will be    $%0.2f' %(after_discount))