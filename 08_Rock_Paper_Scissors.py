#Rock beats scissors
#Scissors beats paper
#Paper beats rock

playerOnePoints = 0;
playerTwoPoints = 0;

while True:
    a = input('Player 1: rock/paper/scissors or \'end\' to end the game: ')
    b = input('Player 2: rock/paper/scissors or \'end\' to end the game: ')
    
    
    if((a == 'rock' and b == 'scissors') or (a == 'paper' and b == 'rock') or
       (a == 'scissors' and b == 'paper')):
        playerOnePoints = playerOnePoints + 1
        print('Player 1 win! Player 1 points: ' + str(playerOnePoints))
        print('')

    elif((a == 'scissors' and b == 'rock') or (a == 'rock' and b == 'paper') or
         (a == 'paper' and b == 'scissors')):
        playerTwoPoints = playerTwoPoints + 1
        print('Player 2 win! Player 2 points: ' + str(playerTwoPoints))
        print('')

    elif(a == 'end' or b == 'end'):
        print('End game')
        print('Player1 points: ' + str(playerOnePoints) + ' | Player 2 points: '+ str(playerTwoPoints))

        check = input('Write \'yes\' if u want to play again: ')
        if(check == 'yes'):
            continue
        else:
            break
    
    else:
        print('Draw!')
