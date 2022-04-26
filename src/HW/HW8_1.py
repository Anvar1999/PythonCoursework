# Write a program with a function that accepts a string as an argument and
# returns a copy of the string with the first character of each sentence capitalized.
# For instance, if the argument is “hello. my name is Joe. what is your name?” 
# the function should return the string “Hello. My name is Joe. What is your name?” 
# The program should let the user enter a string and then pass it to the function. 
# The modified string should be displayed. 

def capitalizer(strng: str):
    sentences = strng.split(". ")
    sentences2 = [sentence[0].capitalize() + sentence[1:] for sentence in sentences]
    string2 = '. '.join(sentences2)
    return string2

print(capitalizer("hello. my name is Joe. what is your name?"))
