num = int(input('Put a number\n'))
check = int(input('Put a second number to divide first number by \n'))

if num % 2 == 0:
    print('You put a even number')
else:
    print('You put a odd number')


if num % 4 == 0:
    print('Number is multiply by 4')
elif num % 2 == 0:
    print('Number is multiply by 2')
else:
    print('Number is odd')

if num % check == 0:
    print(f'{num} is divided by {check}')
else:
    print(f'{num} doesn\'t divide by {check}')
