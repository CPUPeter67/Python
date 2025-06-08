# Program to remove lines starting with any prefix

file1 = open('codingal.text', 'r')
file2 = open('codingalupdated.text', 'w')

# reading each line from original
# text file
for line in file1.readlines():

        # reading all lines that do not 
        # begin with "Coding"
        if not (line.startswith('Coding')):
                
                # printing those lines
                print(line)