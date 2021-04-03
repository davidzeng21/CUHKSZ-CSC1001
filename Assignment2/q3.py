# Return true if the card number is valid:
def isValid(number):
    sum = sumOfDoubleEvenPlace(number) + sumOfOddPlace(number)
    if sum % 10 == 0:
        print("The card number is valid!")
    else:
        print("The card number is invalid!")

# Get the result from Step 2
def sumOfDoubleEvenPlace(number):
    sumOfEven = 0
    number = str(number)
    listOfEven = list()
    for i in range(len(number)-1, -1, -1):
        if i % 2 == 0:
            listOfEven.append(number[i])
    for i in listOfEven:
        sumOfEven += getDigit(int(i)*2)
    return sumOfEven

# Return this number if it is a single digit, otherwise, return
# the sum of the two digits
def getDigit(number):
    digit = 0
    for i in str(number):
        digit += int(i)
    return digit

# Return sum of odd place digits in number
def sumOfOddPlace(number):
    sumOfOdd = 0
    number = str(number)
    listOfOdd = list()
    for i in range(len(number)-1, -1, -1):
        if i % 2 == 1:
            listOfOdd.append(number[i])
    for i in listOfOdd:
        sumOfOdd += int(i)
    return sumOfOdd

while True:
    number=(input("Please Enter Your Credit Card Number: "))
    if number.isdigit and 13 <= len(number) <= 16:
        isValid(int(number))
        break
    else:
        print("Please input a number that have between 13 and 16 digits!")