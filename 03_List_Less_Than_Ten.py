userNum = int(input('Put a number\n'))
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

newList = [num for num in a if num < userNum]
# [output] for [item] in [list] if [filter]

print(newList)
