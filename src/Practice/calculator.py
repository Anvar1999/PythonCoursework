"should solve +-*/"


print("\tCalculator")
print('\t  1 2 3\n\t  4 5 6\n\t  7 8 9\n\t    0')


num1 = int(input("    Enter first number: "))
i = input("    Input one of the operation: ")
num2 = int(input("    Next number: "))
if i == "*":
    total = num1 * num2 
    print("   ",num1,"*",num2,"=",total)
elif i == "/":
    total = num1 / num2 
    print("   ",num1,"/",num2,"=",total)
elif i == "-":
    total = num1 - num2 
    print("   ",num1,"-",num2,"=",total)
elif i == "+":
    total = num1 + num2 
    print("   ",num1,"+",num2,"=",total)
else:
    print("Wrong operation")