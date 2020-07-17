# Fibonacci 0, 1, 1, 2, 3, 5, 8, 13, 21...

num = int(input('How many Fibonacci numbers you would like to see '))

def fib(num):
    a = 0
    b = 1
    if num < 2:
        return 1
    else:
        for i in range(0, num):
            c = a + b
            a = b
            b = c
            print(b)
fib(num)
        
        


