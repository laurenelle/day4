# open file on command line

# char or chr() == converts the int value of a character back to a character

# string.lower()
# ord() == gives you the int value of the char
# iterate through the file like it's a list and 



from sys import argv
script, filename = argv

#from collections import defaultdict
count = 0

text = open(filename)
reading = text.read()

lowered = reading.lower()

text_list = []
text_list += lowered
text_list

alphabet = []
alphabet = range(97,123)
stored_counts = {}
#stored_counts = dict((el,0) for el in alphabet)

for i, v in enumerate(text_list):
	numbered = ord(v)
	if 96 < numbered < 123:
		if numbered in stored_counts:
			stored_counts[numbered] = stored_counts[numbered] + 1
		else:
			stored_counts[numbered] = 1
			
		# count = stored_counts[numbered]
		# stored_counts[numbered] = count+1
#use a dict to store counts

#using a dictionary, which won't work if the dictionary's order changes
# for index, key_letter in enumerate(stored_counts):
# 	print stored_counts[key_letter] # returns final counts

#using a list
for i, letter in enumerate(alphabet):
	print stored_counts[letter]

#print stored_counts [97:121]
		#stored_counts = {numbered: count+1}
		#stored_count = {numbered: text_list.count(numbered)}

 
	  	#counted = text_list.count(letter)
	  
	  	# for letter: 
	  	# 	return counted
	  	#alphabet_dict = {letter: counted}
	  	#print alphabet_dict
	 # 	alphabet_dict = {}
		# alphabet_dict = range (97, 121)

	 	# if numbered == 
	 	# print 
	 	# print text_list.count(v)
	 	# break
	



	#         if v == value:
	#             count += 1

	#.ascii_lowercase # lowercase alphabet


	#lowercase.split(' ')
	# print alphabetical counts
	# read the list only once and store the counts for each letter, then print when complete
	# key = a..z value = count
	# looping on the text file once

	# if ord(v) < 96 and > 123:
	# 	count(v)

	# 	def custom_count(input_list, value):
	#     custom_count(input_list, value) imitates input_list.count(value)
	#     count = 0
	#     for k, v in enumerate(input_list):
	#         if v == value:
	#             count += 1
	#     return count

	# -create a dictionary with keys a..z

	# print the final count
	#text.close()