num  = int(input('Give me number:\n'))

x = range(1, num + 1)

newList = [el for el in x if num % el == 0]
print(newList)
