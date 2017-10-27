filename = 'words.txt'
infile =open(filename, 'r+')
words = infile.read()
words += 'Lolololol\n'
words = "I go first!" + words
print(words)
infile.write(words)
infile.close()
