#A file exists on the disk named students.txt. The file contains several records, and each record contains two fields: 
#(1) the student’s name, and (2) the student’s score for the final exam.
#Write code that deletes the record containing “John Perz” as the student’s name. 

with open('file.txt', 'r') as file:
    text = file.read()


# Delete text and Write
with open('file.txt', 'w') as file:
    # Delete
    new_text = text.replace('Python', '')
    # Write
    file.write(new_text)