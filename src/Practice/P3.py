

#address = """45 crecent
#Ave, 
#Boston, 
#MA 02125"""
#print(address)


#word = ('Hello')
#word = word.upper()
#word1 = ('hello')
#word1 = str.upper(word1)

#print(word,word1)

#print(len(word))
#print(word.capitalize())

#essay = ("this is essay")
#print(essay.title())

#text = (" Hello World ")
#print(text.strip(" "))


#name = input("Enter your name: ")
#print(len(name))


#name = input("Enter your first name: ")
#surname = input("Enter your last name: ")
#concatination = name + " " + surname
#print(concatination)
#print(len(concatination))



#name = input("Enter your First name: ")
#surname = input("Enter your Surname: ")
#surname = str.lower(surname)
#name = str.lower(name)
#full_name = name + " " + surname
#print(full_name.title())

#rhyme = input("Enter nursery rhyme")
#length = len(rhyme)
#print(length)
#start = int(input("Enter starting number of rhyme"))
#ending = int(input("Enter ending number of rhyme"))
#part = (rhyme[start:ending])
#print(part)




#up = input('Enter anything')
#print(str.upper(up))





#first_name = input("Enter your first name")
#length = len(first_name)
#if length < 5:
#    surname = input("Enter your surname")
#    join = first_name+surname
#    print(join.upper())
#else:
#    print(first_name.lower())


word = input('Please enter a word ')

length = len(word)
first = word[0]
rest = word[1:]
final = rest + first 
vovels = ["a", "e", "o", "i", "u"]

if first not in vovels:
    newword = rest + first + "ay"
else:
    newword = rest + first + "way"
print(newword.lower())
