import random

a = random.sample(range(0, 30), 9)
b = random.sample(range(0, 20), 15)

result = [x & y for x in a for y in b if x == y]

print(list(set(result)))
