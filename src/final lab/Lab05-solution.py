###Lab assignments # 5

### Assignment 1
##outfile = open('my_name.txt', 'w') 
##outfile.write('Azadeh Sheikholeslami') 
##outfile.close()


#### Assignment 2
##infile = open('my_name.txt', 'r')
##name = infile.read()
##print(name)
##infile.close()



### Assignment 3
##outfile = open('number_list.txt', 'w')
##for number in range(1, 101):
##    outfile.write(str(number) + '\n')
##outfile.close()




### Assignment 4
##total = 0
##infile = open('number_list.txt', 'r') 
##line = infile.readline()
##
##while line != '': 
##    line = line.rstrip('\n')
##    number = int(line) 
##    total += number
##    print(number)
##    line = infile.readline()
##    
##infile.close()
##print("The total is:", total)






### Assignment 5
### Delete John Perez from the file. 
##
##def main(): 
##    # Create a bool variable to use as a flag. 
##    found = False 
##
##    # Open the original students.txt file. 
##    student_file = open('students.txt', 'r') 
##
##    # Open the temporary file. 
##    temp_file = open('temp.txt', 'w')
##
##    # Read the first record's name field. 
##    name = student_file.readline() 
##
##    # Read the rest of the file. 
##
##    while name != '': 
##        # Read the score field. 
##        score = float(student_file.readline()) 
##
##        # Strip the \n from the name. 
##        name = name.rstrip('\n') 
##
##        # If this is not the record to delete, then 
##        # write it to the temporary file. 
##        if name != 'John Perez': 
##            # Write the record to the temp file. 
##            temp_file.write(name + '\n') 
##            temp_file.write(str(score) + '\n') 
##        else:
##            # Found the name. Set the found flag to True. 
##            found = True 
##
##        # Read the next name. 
##        name = student_file.readline() 
##
##    # Close the student file and the temporary file. 
##    student_file.close() 
##    temp_file.close()
##
##    student_file = open('students.txt', 'w')
##    temp_file = open('temp.txt', 'r')
##
##    # Update the original students.txt file.
##    for line in temp_file:
##        student_file.write(line)
##
##    # Close the student file and the temporary file. 
##    student_file.close() 
##    temp_file.close()
##        
##    # If the search value was not found in the file 
##    # display a message. 
##    if found: 
##        print ('The file has been updated.') 
##    else: 
##        print ('John Perez was not found in the file.')
##
### Call the main function. 
##main()






#####Assignment 6
##
##def main():
##    # Declare variables
##    line = ''
##    counter = 0
##    
##    # Prompt for file name
##    fileName = input('Enter the name of the file: ')
##
##    # Open the specified file for reading
##    infile = open(fileName, 'r')
##
##    # Priming read
##    line = infile.readline()
##    counter = 1
##    
##    # Read in and display first five lines
##    while line != '' and counter <= 5:
##	# Strip '\n'
##        line = line.rstrip('\n')
##        print(line)
##        line = infile.readline()
##        # Update counter when line is read
##        counter +=1  
##
##    # Close file
##    infile.close()
##
### Call the main function.
##main()








###Assignment 7
##
##def main():
##    # Declare variables
##    line = ''
##    counter = 0
##    
##    # Prompt for file name
##    fileName = input('Enter the name of the file: ')
##
##    # Open the specified file for reading
##    infile = open(fileName, 'r')
##
##    for line in infile:
##        counter += 1
##        print(counter, end='')
##        print(':', end=' ')
##        
##        # Strip the '\n' from the end of the line
##        line = line.rstrip('\n')
##        print(line)
##
##    # Close file
##    infile.close()
##
### Call the main function.
##main()







###Assignment 8
##
##def main():
##    # Declare variables
##    line = ''
##    counter = 0
##
##    # Open names.txt file for reading
##    infile = open('names.txt', 'r')
##
##    # Priming read
##    line = infile.readline()
##      
##    # Read in until no more data
##    while line != '':
##        counter += 1
##        line = infile.readline()
##
##    # Close file
##    infile.close()
##
##    # Display the number of names in the file
##    print (counter, 'names were read.')
##
### Call the main function.
##main()








###Assignment 9 Part a
##
##def main():
##    # Local variables
##    name = ''
##    golf_score = 0
##    num_players = 0
##
##    # Prompt user for the number of players
##    num_players = int(input('Enter the number of ' \
##                            'players in the tournament: '))
##
##    # Open golf.txt for writing
##    outfile = open('golf.txt', 'w')
##    
##    # Write data to file
##    for i in range(num_players):
##        # Prompt for name and score
##        name = input('Enter the name of the player: ')
##        golf_score = int(input('Enter the golf score: '))
##
##        # Write data to file
##        outfile.write(name + '\n')
##        outfile.write(str(golf_score) + '\n')
##
##    # Close file
##    outfile.close()
##
### Call the main function.
##main()







###Assignment 9 Part b
##def main():
##    # Local variables
##    line = ''
##    name = ''
##    golf_score = 0
##    num_players = 0
##
##    # Open golf.txt for reading
##    infile = open('golf.txt', 'r')
##
##    # Read first name
##    name = infile.readline()
##    
##    # Read until no data 
##    while name != '':
##        # Read score
##        golf_score = int(infile.readline())
##
##        # Strip '\n'
##        name = name.rstrip('\n')
##
##        # Display data with one line space between the data 
##        # for every two players 
##        print ('Name:', name)
##        print ('Golf Score:', golf_score)
##        
##        # Read next name
##        name = infile.readline()
##
##    # Close file
##    infile.close()
##
### Call the main function.
##main()







###Assignment 10
### Change Julie Milan's score to 100.
##
##def main(): 
##    # Create a bool variable to use as a flag. 
##    found = False 
##
##    # Open the original students.txt file. 
##    student_file = open('students.txt', 'r') 
##
##    # Open the temporary file. 
##    temp_file = open('temp.txt', 'w')
##
##    # Read the first record's name field. 
##    name = student_file.readline() 
##
##    # Read the rest of the file. 
##
##    while name != '': 
##        # Read the score field. 
##        score = float(student_file.readline()) 
##
##        # Strip the \n from the name. 
##        name = name.rstrip('\n') 
##
##        # If this is not the record to delete, then 
##        # write it to the temporary file. 
##        if name == 'Julie Milan': 
##            # Write the new record. 
##            temp_file.write(name + '\n') 
##            temp_file.write('100\n') 
##            # Set the found flag to True. 
##            found = True 
##        else: 
##            # Write the record to the temp file. 
##            temp_file.write(name + '\n') 
##            temp_file.write(str(score) + '\n') 
##
##
##        # Read the next name. 
##        name = student_file.readline() 
##
##    # Close the student file and the temporary file. 
##    student_file.close() 
##    temp_file.close()
##
##    student_file = open('students.txt', 'w')
##    temp_file = open('temp.txt', 'r')
##
##    # Update the original students.txt file.
##    for line in temp_file:
##        student_file.write(line)
##
##    # Close the student file and the temporary file. 
##    student_file.close() 
##    temp_file.close()
##        
##    # If the search value was not found in the file 
##    # display a message. 
##    if found: 
##        print ('The file has been updated.') 
##    else: 
##        print ('Julie Milan  was not found in the file.')
##
### Call the main function. 
##main()








###Assignment 11
##def main():
##    name = input('Enter your name: ')
##    description = input('Describe yourself: ')
##
##    # Create the file.
##    html_file = open('my_page.html', 'w')
##    
##    # Write the HTML
##    write_html(html_file, name, description)
##
##    # Close the file.
##    html_file.close()
##
##def write_html(html_file, name, description):
##    # Write the <html> tag.
##    html_file.write('<html>\n')
##
##    # Write the <head> element.
##    write_head(html_file)
##
##    # Write the body.
##    write_body(html_file, name, description)
##
##    # Write the </html> tag.
##    html_file.write('</html>\n')
##
##def write_head(html_file):
##    html_file.write('<head>\n')
##    html_file.write('<title>My Personal Web Page</title>\n')
##    html_file.write('</head>\n')
##
##def write_body(html_file, name, description):
##    html_file.write('<body>\n')
##    html_file.write('\t<center>\n')
##    html_file.write('\t\t<h1>')
##    html_file.write(name)
##    html_file.write('</h1>\n')
##    html_file.write('\t</center>\n')
##    html_file.write('\t<hr />\n\t')
##    html_file.write(description)
##    html_file.write('\n\t<hr />\n')
##    html_file.write('\t</body>\n')
##
##main()

