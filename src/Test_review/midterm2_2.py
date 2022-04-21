#Answer to the question 2

def main():

    total = 0.0
    length = 0.0
    average = 0.0

    try:
        #Get the name of a file
        filename = input('Enter a file name: ')

        #Open the file
        infile = open(filename, 'r')

        #Read the file's contents
        contents = infile.read().strip().split()

        #Display the file's contents
        print(contents)

        #Read values from file and compute average
        for num in contents:
            amount = float(num)
            total += amount
            length = length + 1

        average = total / len(contents)

        #Close the file
        infile.close()

        #Print the amount of numbers in file and average
        print('The total ', total, '' )
        print('There were ', length, ' numbers in the file.' )
        print(format(average, ',.2f'))

    except IOError:
        print('An error occurred trying to read the file.')

    except ValueError:
        print('Non-numeric data found in the file')

    except:
        print('An error has occurred')


main()