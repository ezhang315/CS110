import stringoperations

'''
Written by: Kevin Wallace
Date: 3/17/17

counts the number of each letter of the alphabet in strings
creates a random string of a user-determined length

requests one user input

outputs to the monitor: character counts for various strings, and one random string
'''


def main():
	# testing countCharacters with various strings
	print(stringoperations.countCharacters('Banana'))
	print(stringoperations.countCharacters('I nip in; pin Pippin'))
	print(stringoperations.countCharacters("Blowzy night-frumps vex'd Jack Q"))
	# getting the length of the random string
	# printing the random string
	# counting the string's characters
	str_len = int(input("Enter the length of a random string:  "))
	rand_str = stringoperations.createRandomString(str_len)
	print(rand_str)
	print(stringoperations.countCharacters(rand_str))

main()
