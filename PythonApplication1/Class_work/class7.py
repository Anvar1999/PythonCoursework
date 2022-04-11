"""
#Open a file file_name
outfile = open('file_name.txt', 'w')

#these tree text will be in the file_name file
outfile.write('This is a test\n')
outfile.write('This is a test\n')
outfile.write('This is a test\n')


#close the file
outfile.close()
"""

"""
#program for read the file
def main():

    #Open a file infile, r for reading mode
    infile = open('file_name.txt', 'r')

    file_content = infile.read() 


    #close the file
    infile.close()
    print(file_content)

main()
"""


def main():

    #Open a file infile, r for reading mode
    infile = open('file_name.txt', 'r')

    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    #close the file
    infile.close()
    print(line1)
    print(line2)
    print(line3)

main()