name = input('Enter your name\n')
age = int(input('Enter your age\n'))
year = (2020 - age) + 100
multiplyBy = int(input('Message copies\n'))

print(f'{name} you will have 100 yers old in {year}\n')
print('Copies: \n')

for i in range(0, multiplyBy):
    print(f'{name} you will have 100 yers old in {year}\n')
