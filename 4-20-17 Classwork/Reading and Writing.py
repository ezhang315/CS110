infile = open('applic.txt', 'r')
info = infile.read()
text = ''
current_line = 0
while info[current_line] != '':
    print(info[current_line])
    items = info[current_line].split()
    print('line split')
    print(items)
    text += (items[1] + ',' + items[0] + '\n')
    current_line += 1
    print('line passed')
infile.close()
newfile = open('applic-new.txt', 'w')
newfile.write(text)
newfile.close()
