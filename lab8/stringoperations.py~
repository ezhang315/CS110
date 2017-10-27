import random
'''
Written by: Kevin Wallace
Date: 3/17/17

A module that can create a string consisting of random characters of an inputted length and count the number of appearances of all letters in a string
'''

# creates a string made of random characters from a-Z including space
# param num is an integer
# returns string, the random string
def createRandomString(num):
	string = ''
	# making a list of ascii values of all letters and space
	chars = [32] + list(range(65, 91)) + list(range(97, 123))
	for i in range(num):
		# grabbing a random value from the list and adding its corresponding character to the string
		value = random.choice(chars)
		string += chr(value)
	return string

# counts the number of appearances of every letter of the alphabet in a string
# param count_str is a string to be analyzed
# returns count
# count is a list of values corresponding to the number of appearances of every letter in sount_str
def countCharacters(count_str):
	count = [0] * 26
	for i in count_str:
		if 65 <= ord(i.upper()) <= 90:
			count[ord(i.upper()) - 65] += 1
	return count



