txt = input('Put a string ').lower()

#start at string length, end at position 0 move with the step -1
if txt == txt[::-1]:
    print('This is a palindrome')
else:
    print('This is not a palindrome')
