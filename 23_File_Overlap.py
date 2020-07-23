prime_numbers = []
happy_numbers = []

with open('primenumbers.txt', 'r') as f:
    for num in f:
        prime_numbers.append(int(num))


with open('happynumbers.txt', 'r') as f:
    for num in f:
        happy_numbers.append(int(num))


print(list(set(prime_numbers) & set(happy_numbers)))
