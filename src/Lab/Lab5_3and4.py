
#3) Write code that does the following: opens an output file with the filename number_list.txt,
#uses a loop to write the numbers 1 through 100 to the file, then closes the file.
# create the file


#4) Write code that does the following: opens the number_list.txt file that was created by the code you wrote in question 3,
#reads all the numbers from the file, adds all the numbers read from the file and displays their total, then closes the file.



filename = "number_list.txt"

# for writing, we create the output file:

outPutfile = open(filename, "w")

# Writing numbers from 1-100

for item in range(1,101):

 outPutfile.write((str)(item))

outPutfile.close()

# printing the contents to verify it worked correctly

infile = open(filename, "r") #note the "r" indicates the mode

fileContents = infile.read()

infile.close()

print(fileContents)