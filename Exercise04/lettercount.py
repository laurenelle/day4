# open file on command line

# char or chr() == converts the int value of a character back to a character

# string.lower()
# ord() == gives you the int value of the char
# iterate through the file like it's a list and 
from sys import argv


string.ascii_lowercase # lowercase alphabet

script, filename = argv


text = open("inputfile.txt")
reading = text.read()

lowercase = reading.lower()

#print lowercase.strip()

lowercase.split(' ')
# print alphabetical counts

text.close()