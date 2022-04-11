  #Write a program that opens the my_name.txt file that was created by the program in problem 1, reads your name from the file, 
  #displays the name on the screen, then closes the file.

def main():

    #Open a file infile, r for reading mode
    infile = open('my_name.txt', 'r')

    file_content = infile.read() 


    #close the file
    infile.close()
    print(file_content)

main()