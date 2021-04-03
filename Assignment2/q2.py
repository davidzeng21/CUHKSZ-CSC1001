def reverse(x):
    return int(str(x)[::-1])

def isPrime(value):
    test = 2
    while test < value:
        if value % test != 0:
            test += 1
        else:
            return 0
    return 1

i = 13
count = 1
while count < 101:
    if isPrime(i) and i != reverse(i):
        if isPrime(reverse(i)):
            print(str(i), end="\t")
            if count % 10 == 0:
                print()
            count += 1
            i += 1
        else:
            i += 1
    else:
        i += 1

