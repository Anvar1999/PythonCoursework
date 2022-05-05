###Lab assignments # 9

### Assignment 1

##if 'James' in dct:
##    print(dct['James'])
##else:
##    print('James is not in the dictionary.')



### Assignment 2
##if 'Jim' in dct:
##    del dct['Jim']
##else:
##    print('Jim is not in the dictionary.')





### Assignment 3

##set3 = set1.union(set2)
##
##set4 = set1.intersection(set2)
##
##set5 = set1.difference(set2)
##
##set6 = set2.difference(set1)
##
##set7 = set1.symmetric_difference(set2)




    

### Assignment 4
##again = 'y'
##number_list = []
##
##while again == 'y':
##    number = float(input('Enter a number: '))
##    number_list.append(number)
##    again = input('Do you want to continue? Enter y for yes.')
##
##number_set = set(number_list)
##print('The set of unique numbers is:', number_set)


### Assignment 5
##dct = {}
##for i in range(5):
##    key = input('Please enter a key: ')
##    value = input('please enter a value: ')
##    dct[key] = value
##
##print("Your dictionary is:", dct)



### Assignment 6
##MENU = {'sandwich' : 10, 'tea' : 7, 'salad' : 9}
##dish = ' '
##total = 0
##
##while dish != 'end':
### Getting an order from the user
##    dish = input('Order: ')
##
### If the dish is in the menue, show the cost
### Otherwise, infor the user
##    if dish in MENU:
##        total += MENU[dish]
##        print(dish, "costs $", MENU[dish], ", total is $", total)
##    elif dish != 'end':
##        print('Sorry, we are out of', dish,'today.')
##
### The thank you note
##print('Thank you for your order!')








### Assignment 7

##def main():
##    # Set up empty dictionary
##    dict_words = {}
##
##    # Get input text
##    input_file = open('text.txt', 'r')
##    text = input_file.read()
##    words = text.split()
##
##    
##    # For each word in the text increase its value in the dictionary
##    for word in words:
##        if word in dict_words:
##            dict_words[word] += 1
##        else:
##            dict_words[word] = 1
##    
##
##    # Display results
##    print(format('word', '15'),'\t',format('occurrences','15'))
##    print('----------------------------------------------')
##    for word in dict_words:
##
##        print(format(word,'15'), format(dict_words[word], '15'))
##
### Call the main function.
##main()



### Assignment 8
##def main():
##    # Get input text of first file and create set containing 
##    # its unique words
##    file1 = open('text1.txt', 'r')
##    text1 = file1.read()
##    file1.close()
##    words1 = text1.split()
##    set1 = set(words1)
##
##    # Get input text of second file and create set containing its 
##    # unique words
##    file2 = open('text2.txt', 'r')
##    text2 = file2.read()
##    file2.close()
##    words2 = text2.split()
##    set2 = set(words2)
##
##    # Obtain the union of the sets and print the items in it
##    union = set1.union(set2)
##    print('These are the unique words that are ' \
##          'contained in both files:')
##    for item in union:
##        print(item)
##    print()
##
##    # Obtain the intersection of the sets and print the items in it
##    intersection = set1.intersection(set2)
##    print('These are the words that appear both files:')
##    for item in intersection:
##        print(item)
##    print()
##
##    # Obtain the difference between set1 and set2 and 
##    # print the items in it
##    difference1 = set1.difference(set2)
##    print('These are the words that appear in the first file' \
##          ' but do not appear in the second file:')
##    for item in difference1:
##        print(item)
##    print()
##
##    # Obtain the difference between set2 and set1 and 
##    # print the items in it
##    difference2 = set2.difference(set1)
##    print('These are the words that appear in the second file' \
##          ' but do not appear in the first file:')
##    for item in difference2:
##        print(item)
##    print()
##
##    # Obtain the symmetric difference between set1 and set2 
##    # and print the items in it
##    sym_diff = set1.symmetric_difference(set2)
##    print('These are the words that appear in the first' \
##          ' file or the second file but do not appear in' \
##          ' the both files:')
##    for item in sym_diff:
##        print(item)
##    print()
##
### Call the main function.
##main()




