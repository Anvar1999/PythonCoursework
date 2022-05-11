import random

# num = random.randint(1,100)
# print(num)

# fruit = random.choice("Apple","orange","vatermalen","strawberry","mandarin")
# print(fruit)


# ht = random.choice("h","t")
# choose = input("h or t")
# if choose == ht:
#     print("You win")
# else:
#     print("Bad luck")

# print("Computer chose", ht)



# number = random.randint(1,5)
# pick = int(input("Pick a number:"))
# if number == pick:
#     print("Well done!")
# elif pick > number:
#     print("Too high")
#     pick = int(input("Pick another number:"))
#     if pick == number:
#         print("Correct")
#     else:
#         print("You loose")
# else:
#     print("Too low")
#     pick = int(input("Pick another number:"))
#     if pick == number:
#         print("Correct")
#     else:
#         print("You loose")


# number = random.randint(1,10)
# enter = int(input("enter a number"))
# while number != enter:
#     enter = int(input("enter a number"))



# number = random.randint(1,10)
# enter = int(input("enter a number"))
# while number != enter:
#     if enter > number:
#         print("too high")
#     elif enter < number:
#         print("too low")

#     enter = int(input("enter a number"))



# score = 0

# for i in range(1,6): 
#     num  = random.randint(1,10)
#     num2 = random.randint(1,10)

#     exp = num + num2
#     print(num, "+", num2, "=", end =" ")
#     exp1 = int(input())
#     if exp == exp1:
#         score = score + 1


# print("You have found %.0f times out of 5" %score)




colors = ["Blue","Red","Yellow","Green","Silver"]
print(colors)
take = random.choice(colors)
pick = input("Pick one")
while pick != take:

    if pick == take:
        print("well done")
    else:
        print("I bet you are %s with envy" %take)
    pick = input("Pick one")



