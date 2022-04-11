#This exercise assumes you have completed Programming Exercise 1.
# Write another program that reads the random numbers from the file random_numbers.txt, displays the numbers, then displays the following data:
#a.	The total (sum) of the numbers
#b.	The number of random numbers read from the file
#c.	The average value of the numbers read from the file

def main():

    #Open a file infile, r for reading mode
    infile = open('random_numbers.txt', 'r')

    file_content = infile.read() 
    
    
    #close the file
    infile.close()
    print(file_content)

main()