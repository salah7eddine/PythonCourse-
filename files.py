# Python has functions for creating, reading, updating, and deleting files.


# open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name: ', myFile.name)
print('Is closed: ', myFile.close)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I love Python')
myFile.write(' and JavaScript')
myFile.close()

# Append to file 
myFile = open('myfile.txt', 'a')
myFile.write(' , I also like Java & Spring')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(100)
print(text)


