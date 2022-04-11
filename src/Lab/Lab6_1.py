#Write code that does the following: opens an output file with the filename number_list.txt, 
#uses a loop to get numbers from the user, and write the numbers to the file, then closes the file.



def main():

    outfile = open('number_list.txt','w')
    line = float(input('Enter a number: '))
    while line != 0: 
        outfile.write(str(line) +'\n')
        line = float(input('Enter a number: '))
    
        

    outfile.close()

main()

