def numStr():
    num_str = ''
    for i in range(1,101):
        if i == 100:
            num_str += str(i)
        else:
            num_str += str(i) + ','
    return num_str

def bingMods(bin_str):
    print(bin_str[:3])
    print(bin_str[4:6] + bin_str[7])
    print(bin_str[0] + bin_str[8] + bin_str[5] + bin_str[7])

def main():
    print(numStr())
    binghamton = 'Binghamton'
    bingMods(binghamton)
    results = 'average: 0.8475'
    ind = results.find(':')
    average = float(results[ind + 2:])
    print(average)

main()
