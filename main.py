import math


def zad1(a, b, c, d, e):
    P = a*b*1.1
    n= math.ceil(P/(c*d))
    return math.ceil(n/e)

def zad2(*arg):
    for i in arg:
        if i <= 1:
            print(str(i) + " nie jest liczbą pierwszą")
        else :
            for j in range(2, i+1):
                if i==j:
                    print(str(i) + " jest liczbą pierwszą")
                    break
                if i%j==0:
                    print(str(i) + " nie jest liczbą pierwszą")
                    break

def zad3(a, k, alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']):
    a = a.lower()
    result =""

    for c in a:
        if c in alfabet:
            index = alfabet.index(c)
            l = alfabet[(index+k)%len(alfabet)]
            result+=l
        else:
            result+=c
    print(result)
if __name__ == '__main__':
    zad3("The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll", 5, ['a', 'b'])
