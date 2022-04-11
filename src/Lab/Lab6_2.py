def main():
    total = 0
    try:
    #Open a file infile, r for reading mode
        infile = open('number_list.txt', 'r')
        file_content = infile.read() 
        for line in infile:
            number = float(line)
            total += number

    #close the file
        infile.close()
        print(file_content)
        print('The total of number:', format(total, ',.2f'))
    except IOError as err:
        print(err)
    except ValueError:
        print('The file should contain only numeric')
    except Exception as err:
        print(err)
    else: 
        print('The total of number:', format(total, ',.2f'))

main()
"""
def main():
    total = 0.0

    filename = input('Enter the filename: ')
    try:
        temp = 7/10
        infile = open(filename, 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print('The total sales is:', format(total, ',.2f'))
    except IOError as err:
        print(err)
    except ValueError:
        print('The file should contain only numeric')
    except Exception as err:
        print(err)
    else: 
        print('The total sales is:', format(total, ',.2f'))
  
            
    
main()
"""