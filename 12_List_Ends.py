import random

def createRandomList():
    randomList = random.sample(range(10, 80), 10)
    return randomList

def firstAndLastEl(a):
    newList = [a[0], a[-1]]
    print(newList)
    
firstAndLastEl(createRandomList())
