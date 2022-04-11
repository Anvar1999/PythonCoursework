"""
#try except 
def main():
    total = 0.0

    filename = input('Enter the filename: ')
    try:
        infile = open(filename, 'r')
        for line in infile:
            amount = float(line)
            total += amount
        infile.close()
        print('The total sales is:', format(total, ',.2f'))
    except FileNotFoundError:
        print('There ws an issue with the file')
            
    
main()
"""
"""
# exception types  
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
    except IOError:
        print('There ws an issue with the file')
    except ValueError:
        print('The file should contain only numeric')
    except:
        print('An error occured.')
  
            
    
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