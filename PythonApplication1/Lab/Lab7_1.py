#Write a function that accepts a list as an argument (assume the list contains integers)
#and returns the total of the values in the list.



def main():

    list = [1,2,3,4,5]
    accept(list)
    print("List: ", list)

def accept(list):

    total = 0

    for elem in list: total += elem

    print("Total ", total)
     
main()