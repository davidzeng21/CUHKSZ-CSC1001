def sqrt(n):
    lastGuess = n
    while True:
        nextGuess = (lastGuess + (n / lastGuess)) / 2
        if abs(nextGuess-lastGuess) <= 0.0001:
            break
        else:
            lastGuess = nextGuess
    return nextGuess

while True:
    try:
        n = float(input("Please input a positive number: "))
        if n > 0:
            lastGuess = n
            break
        else:
            print("Please input a positive number!")
    except:
        print("Please input a positive number!")

asr = sqrt(n)
print("The approximated square root of", n, "is", asr)