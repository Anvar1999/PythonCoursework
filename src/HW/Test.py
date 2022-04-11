"""
score = int(input('Input the number: '))

if score > 100 or score < 0:
    print('outside of the range')
else:
    print('inside the range')
"""
"""
x= 3
y=1

if(x>=10 and y!=0) or (x+y)<=5:
    print("True")
else: 
    print('False')
"""

"""
total = 0
for i in range(1,3):
    for j in range(2,4):
        total = total + (i-j)

print(total)
"""
"""
ask_user = int(input("How many Celsius would you like to enter?\n"))
n = ask_user
print("please enter",str(ask_user) + " integers" )
min = 999
max = 0
for i in range(0, n):
    k = int(input())
    if k < min:
       min = k
    if k > max:
        max = k
while min < max: 
    print("Celsius", min)
    min += 1

print("Celsius", max)
"""
"""
def main():
    x,y,z = magic(2, c = 1, b = 3)
    print("the answers are:", x, y, z)
def magic(a, b, c):
    num1 = a**2
    num2 = b**2
    num3 = c**2
    return num1, num2, num3
main()  
"""
"""
number = int(input("enter"))
while number > 1 and number < 100:
    print('valid')
    number = int(input('enter a value'))
print('invalid')
"""
"""
def main():
    try:
        total = int(input("enter total?"))
        num_items = int(input("number of items"))
        average = total/num_items
    except ZeroDivisionError:
        print('ERROR: cannot have 0 items')
    except ValueError:
        print('ERROR: number of items cannot be negative')

main()
"""
