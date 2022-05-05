# Solutions of Lab08

### Assignment 1
##counter = 0
##for ch in mystring:
##	    if ch == ' ':
##	        counter +=1
##print('The number of space characters is', counter)





### Assignment 2
##counter = 0
##for ch in mystring:
##    if ch.isdigit():
##        counter +=1
##print('The number of digits is', counter)





### Assignment 3
##counter = 0
##for ch in mystring:
##    if ch.islower():
##        counter +=1
##print('The number of lowercase characters is', counter)






### Assignment 4
##def main():
##    # Receive user input
##    full_name = input ('Enter your full name: ')
##
##    # Split according to spaces
##    name = full_name.split()
##
##    # The first character of each name is an initial
##    for string in name:
##        print(string[0].upper(), sep='', end='')
##        print('.', sep=' ', end='')
##
### Call the main function.
##main()
    








### Assignment 5
##def main():
##    # Get a string of numbers as input from the user.
##    number_string = input('Enter a sequence of digits ' \
##                          'with nothing separating them: ')
##
##    # Call string_total method, and store the total.
##    total = string_total(number_string)
##
##    # Display the total.
##    print('The total of the digits in the ' \
##          'string you entered is', total)
##
##
### The string_total method receives a string and returns
### the total of all the digits contained in the string.
### The method assumes that the string does not contain
### non-digit characters
##def string_total(string):
##    # Local variables
##    total = 0
##    number = 0
##
##    # Step through each character in the string.
##    for i in range(len(string)):
##        # Convert the character to an integer.
##        number = int(string[i])
##        # Add the value to the running total.
##        total += number
##
##    # Return the total.
##    return total
##
### Call the main function.
##main()





#### Assignment 6
##def main():
##    
##    # Local variables
##    day = 0
##    month_num = 0
##    month_name = ''
##    date_string = ''
##    month_list = ['January', 'February','March',
##                  'April', 'May','June', 'July',
##                  'August', 'September', 'October',
##                  'November', 'December']
##    
##    # Get the date in mm/dd/yyyy format as input from the user.
##    date_string = input('Enter a date in the format mm/dd/yyyy: ')
##
##    # Split date_string.
##    date_list = date_string.split('/')
##
##    # Obtain month and day numbers.
##    month_num = int(date_list[0])
##    day = date_list[1]
##    year = date_list[2]
##
##    # Get month_name.
##    month_name = month_list[month_num - 1]
##
##    # Create string for long date format.
##    long_date = month_name + ' ' + day + ', ' + year
##
##    # Display long date format.
##    print(long_date)
##
### Call the main function.
##main()







### Assignment 7
##def main():
##    # Get the string as input from the user.
##    user_string = input('Enter a string for the program ' \
##                        'to capitalize sentences: ')
##
##    # Call the capitalize function, storing the result.
##    result = capitalize(user_string)
##
##    # Display the result.
##    print(result)
##
### The capitalize method receives a string and returns
### the same string with the first letters of all
### sentences capitalized
##def capitalize(string):
##    # Initialize variables
##    result = ''
##    new_sentence = True
##    result_word = ''
##
##    # Obtain all the words in the string.
##    words = string.split()
##
##    # For each word in the string:
##    for item in words:
##       # The word is the beginning of a new sentence.
##        if new_sentence:
##            # Create new word where first letter is capitalized.
##            result_word = item[0].upper() + item[1:]
##        else:
##            # Do nothing.
##            result_word = item
##
##        # Add resulting word to the string.
##        result = result + result_word + ' '
##
##        # If the last character in the word indicates 
##        # the end of a sentence, set flag to ensure
##        # that next word will be treated as new sentence.
##        if item[-1] == '.' or item[-1] == '?' or item[-1] == '!':
##            new_sentence = True
##        else:
##            new_sentence = False
##
##    # Return the result.
##    return result
##
### Call the main function.
##main()





   
# Assignment 8
### Function assumes that the input includes no proper nouns.
##def main():
##    # Set up local variables.
##    result = ''
##    
##    # Receive user input.
##    user_string = input('Enter a string: ')
##
##    # Copy first letter in the string in its capitalized form.
##    result = result + user_string[0]
##    
##    for i in range(1, len(user_string)):
##
##        ch = user_string[i]
##
##        # If the next character is in upper case set a space
##        # for the new word and convert the letter to lower case.
##        if ch.isupper():
##            ch = ch.lower()
##            result = result + ' '
##
##        result = result + ch
##
##    print(result)
##
### Call the main function.
##main()







### Assignment 9
##def main():
##    # Local variables
##    vowels = 0
##    consonants = 0
##
##    # Get the string as input from the user.
##    user_string = input('Enter a string: ')
##
##    # Call the vowel_counter function,
##    # storing the result.
##    vowels = vowel_counter(user_string)
##    
##    # Call the consonant_counter function,
##    # storing the result.
##    consonants = consonant_counter(user_string)
##
##    # Display the results.
##    print('The string you entered includes', vowels, \
##          'vowels and', consonants, 'consonants.')
##
### The vowel_counter method receives a string and
### returns the number of vowels in the string.
##def vowel_counter(string):
##    # Set up local variables
##    count = 0
##    vowels = 'aeiou'
##
##    # For each character,
##    # determine if it is a vowel.
##    for ch in string:
##        if vowels.find(ch) >= 0:
##            count = count + 1
##
##    # Return the number of vowels in the string.
##    return count
##        
### The consonant_counter method receives a string and
### returns the number of consonants in the string.
##def consonant_counter(string):
##    # Set up local variables
##    count = 0
##    consonants = 'bcdfghjklmnpqrstvwxyz'
##
##    # For each character,
##    # determine if it is a consonant.
##    for ch in string:
##        if consonants.find(ch) >= 0:
##            count = count + 1
##
##    # Return the number of consonants in the string.
##    return count
##
### Call the main function.
##main()








### Assignment 10	

### Function displays the character that appears most frequently
### in the string. If several characters have the same highest
### frequency, displays the first character with that frequency.
##def main():
##
##    # Set up local variables
##    count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
##    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##    index = 0
##    frequent = 0
##
##    # Receive user input.
##    user_string = input('Enter a string: ')
##
##    for ch in user_string:
##
##        ch = ch.upper()
##
##        # Determine which letter this character is.
##        index = letters.find(ch)
##        if index>=0:
##
##            # Increase counting array for this letter.
##            count[index] = count[index] + 1
##
##    for i in range(len(count)):
##        if count[i] > count[frequent]:
##            frequent = i
##
##    print('The character that appears most frequently' \
##          ' in the string is ', letters[frequent], '.', \
##          sep='')
##    print(count)
##
### Call the main function.
##main()






