#Write a program that opens an output file with the filename my_name.txt, writes your name to the file, then closes the file.

outfile = open('my_name.txt', 'w')

#these tree text will be in the file_name file
outfile.write('Anvar Ermatov')



#close the file
outfile.close()