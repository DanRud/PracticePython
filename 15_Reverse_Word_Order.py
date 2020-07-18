stri = input('Put a long string: ')

def reverseString(stri):
    return ' '.join(stri.split()[::-1])

print(reverseString(stri))
    
