
# first = input("enter your first name: ")
# print(len(first))
# surname = input("enter your surname: ")
# print(len(surname))
# join = first + " " + surname
# print(join)
# print(len(join))


# subject = input("enter your favourite subject: ")
# for letter in subject:
#     print(subject, end = "-")


# text = "This is beatiful city"
# print(text)
# start = int(input("enter starting point: "))
# end = int(input("enter ending point: "))
# print(text[start:end])


# word = input("Enter a word in uppercase: ")
# tryagain = False
# while tryagain == False:
#     if word.isupper():

#         print("Thank you! ")
#         tryagain = True
#     else:
#         word = input("Try again: ")




# postcode = input('Enter your postcode: ')

# start = postcode[0:2]
# print(start.upper())




# count = 0
# name = input("Enter your name: ")

# name = name.lower()
# for x in name:
#     if x == 'a' or x == 'e' or x == 'i' or x == 'u' or x == 'o':
#         count = count + 1
# print(count)


# password = input("Enter a password: ")
# again = input("Enter again: ")
# if password == again:
#     print("Thank you")
# elif password.lower() == again.lower():
#     print("they must be the same case")
# else:
#     print("Incorrect")





word = input("Enter a word: ")
word1 = len(word)
for x in word[word1 ::-1]:
    print(x)


    
