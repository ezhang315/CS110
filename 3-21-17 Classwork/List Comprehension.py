def main():
    sentence = "the quick brown fox jumps over the lazy dog"
    words = sentence.split()
    word_lengths = [len(word) for word in words if word != 'the']
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    newlist = [int(x) for x in numbers if x > 0]
    print(word_lengths, newlist, sep='\n')

main()
