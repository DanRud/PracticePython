randomList = [1, 1, 2, 3, 5, 5, 7, 8, 11, 32, 33, 55, 56, 56]

def removeDuplicate(randomList):
    return list(set(randomList))

print(removeDuplicate(randomList))

def removeDuplicateTwo(randomList):
    newList = []
    for i in randomList:
        if i not in newList:
            newList.append(i)
    return newList

print(removeDuplicateTwo(randomList))
