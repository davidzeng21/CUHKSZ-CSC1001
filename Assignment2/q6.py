import random

def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i]-nextX) in (0, nextY-i):
            return True
    return False

def queens(number = 8, state=()):
    for position in range(number):
        if not conflict(state, position):
            if len(state) == number - 1:
                yield(position, )
            else:
                for result in queens(number, state + (position, )):
                    yield(position, ) + result

def printSampleSolution():
    # Pick one sample solution
    possibleSolutions=list(queens())
    sampleSolution=random.sample(possibleSolutions,1)
    SampleList=list(sampleSolution[0])

    # Print the solution
    for indexOfX in SampleList:
        count = 0
        while count < indexOfX:
            print('| ',end='')
            count += 1
        while count == indexOfX:
            print('|Q',end='')
            count += 1
        while count > indexOfX and count < 8:
            print('| ',end='')
            count += 1
        while count == 8:
            print('|',end='')
            count += 1
            print()

printSampleSolution()