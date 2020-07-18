import random

def compare_numbers(number, userNum):
    cowbulls = [0,0]
    for i in range(len(number)):
        if number[i] == userNum[i]:
            cowbulls[1] += 1
        else:
            cowbulls[0] += 1
    return cowbulls


def main():
    play = True
    number = str(random.randint(0,9999))

    while play:
        userNum = input('Guess a 4 digit number or exit: ')
        if userNum == 'exit':
            break
        cowbullcount = compare_numbers(number, userNum)

        print('You have '+ str(cowbullcount[0]) + ' cows, and ' + str(cowbullcount[1]) + ' bulls')

        if cowbullcount[1] == 4:
            play = False
            print('You win game, the number was ' + str(number))
            break
        else:
            print('Try again')
        

if __name__ == "__main__":
    main()
