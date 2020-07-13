import random

score = 0;
randomNum = random.randint(1,9)
while True:
    userNum = input('Guess random number: ')
    if userNum == 'exit':
        print('End game, your score: ' + str(score))
        break;
    elif int(userNum) > randomNum:
        print('Number is too high')
        continue;
    elif int(userNum) < randomNum:
        print('Number is too low')
        continue;
    else:
        print('Correct number!')
        score = score + 1
        randomNum = random.randint(1,9)
        continue;
