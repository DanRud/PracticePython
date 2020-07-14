num = int(input('Put a number and check whether the number is prime or not '))

def numPrime(num):
    if num > 1:
        for i in range(2, num + 1):
            if (num % i) == 0:
                print('This number is not prime number')
                break;
            else:
                print('This number is prime number')
                break;
    else:
        print('This number is not prime number')

numPrime(num)

