#Part 2
import re
def main(): #This is main function,
    #created the variable a_string
    a_string = ("Like happy like birthday Yep summer is totally here lol yep happy summer")
    #created the variable words_to_remove, 
    words_to_remove = ['like', 'whatever', 'lol', 'yep', 'totally']
    #call fucntion
    remove_words(a_string, words_to_remove) 

def remove_words(parametr_1, parametr_2): #remove_words function containing 2 parameters which passed as argument (a_string, words_to_remove) 
    #fucntion to take out the words
    resultwords  = [word for word in re.split("\W+",parametr_1) if word.lower() not in parametr_2] 
    print(resultwords)#print the result after taking out the words
    outfile = open('remove_words.txt', 'w')#to create a outfile and write the result into outfile

    # will be in the file_name file
    outfile.write(str(resultwords))



    #close the file
    outfile.close()


    return resultwords



main()


