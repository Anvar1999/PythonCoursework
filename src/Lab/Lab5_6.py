#Write a program that asks the user for the name of a file. 
#The program should display only the first five lines of the file’s contents. 
#If the file contains less than five lines, it should display the file’s entire contents.

def main():
    filename = input("enter the file name")
    num1 = int(input('Enter a number 1: '))
    num2 = int(input('Enter a number 2: '))
    num3 = int(input('Enter a number 3: '))
    num4 = int(input('Enter a number 4: '))
    num5 = int(input('Enter a number 5: '))

    outfile = open(filename,'w')

    outfile.write(str(num1) +'\n')
    outfile.write(str(num2) +'\n')
    outfile.write(str(num3) +'\n')
    outfile.write(str(num4) +'\n')
    outfile.write(str(num5) +'\n')

    outfile.close()

    infile = open(filename, "r") #note the "r" indicates the mode

    fileContents = infile.read()

    infile.close()

    print(fileContents)

main()