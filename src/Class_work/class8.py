# file created
"""
def main():
    num1 = int(input('Enter a number 1: '))
    num2 = int(input('Enter a number 2: '))
    num3 = int(input('Enter a number 3: '))

    outfile = open('numbers.txt','w')

    outfile.write(str(num1) +'\n')
    outfile.write(str(num2) +'\n')
    outfile.write(str(num3) +'\n')

    outfile.close()

main()
"""
# read file code
"""
def main():
    infile = open('numbers.txt', 'r')
    string_input = infile.readline()
  
    value = int(string_input)
    print(value)

    infile.close()

main()
"""
"""
def main():
    infile = open('numbers.txt', 'r')

  
    value = int(infile.readline())
    print(value)

    infile.close()

main()
"""

def main():

    sales_file = open('sales.txt', 'r')

    line = sales_file.readline()

    while line != '':
        amount = float(line)
        print('Amount: S', format(amount, '.2f'))

        line = sales_file.readline()

        sales_file.close()

main()
