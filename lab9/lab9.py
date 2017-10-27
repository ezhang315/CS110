import random
'''
CS 110 Lab 9 - Dictionaries
Written by: Kevin Wallace
Date: 3/24/17

Generates a cipher that encrypts inputted messages
Closes if the inputted message is 'q'
'''

# creates a random encryption cipher for ascii characters between 32 and 127
# every character has a unique key
# returns cipher, a dictionary
def createCipher():
	ascii_values = [chr(i) for i in range(32, 127)]
	key_values = [chr(i) for i in range(32, 127)]
	cipher = {}
	for i in ascii_values:
		new_key = random.choice(key_values)		
		cipher[i] = new_key
		key_values.pop(key_values.index(new_key))
	return cipher

# encrypts a given string using a given cipher
# param text is the string to be encrypted
# param cipher is the dictionary to be used to encrypt the string
# returns either string error or string encrypted_string
# error is a string that tells the user that a message couldn't be encrypted
# encrypted_string is the newly encrypted string		
def encrypt(text, cipher):
	encrypted_string = ""
	for i in text:
		if 32 <= ord(i) < 127:
			encrypted_string += cipher[i]
		else:
			error = "MessageError: Message contained invalid character(s)"
			return error
	return encrypted_string

# prints a cipher with visually pleasing formatting
# param cipher is a dictionary
# returns keys, a string containing the keys of the cipher
# returns values, a string containing the values of the cipher
def printCipher(cipher):
	keys = ''
	values = ''
	for i in cipher.keys():
		keys += i
	for j in cipher.values():
		values += j
	print("Cipher: ", keys, values, "=" * 80, sep='\n')

# creates a cipher, prints it to the monitor, then encrypts user inputted strings with that cipher until a quit message 'q' is entered
# calls createCipher(), printCipher(), and encrypt()
# requests string inputs from the user
def main():
	cipher = createCipher()
	printCipher(cipher)
	done = False
	while not done:
		message = input("Enter the message to be encrypted:  ")
		if message == "q":
			done = True
			print("Goodbye!")
		else:
			print(encrypt(message, cipher))
main()
