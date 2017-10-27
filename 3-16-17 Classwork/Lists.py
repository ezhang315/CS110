def sumOfSquares(xs):
    sum = 0
    for i in xs:
        sum += (i ** 2)

    return sum

def main():
    a = [1, 2, 3]
    a.append('apple')
    a.append(76)
    a[2:2] = ['cat']
    a[0:0] = [99]
    count76 = 0
    for i in a:
        if i == 76:
            count76 += 1
    a.remove(76)
    a[a.index('apple')] = 'orange'
    print(a)

main()
