import random

passLength = int(input('How many length password you need? Put a number: '))

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

def generatePassword(passLength):
    password = ' '.join(random.sample(s, passLength))
    return password

print(generatePassword(passLength))
