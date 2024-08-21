import random, sys

wins = 0
losses = 0
ties = 0

# Главный цикл
while True:
    print('%s побед, %s поражений, %s ничьих' % (wins, losses, ties))

    while True:
        print('Выберите действие: (к)амень, (н)ожницы, (б)умага, (в)ыход \n')
        playerMove = input()
        if playerMove == 'в':
            sys.exit()
        if playerMove == 'к' or playerMove == 'н' or playerMove == 'б':
            break
        print('Введите "к", "н" или "б" ')

    if playerMove == 'к':
        print('КАМЕНЬ И ...')
    elif playerMove == 'н':
        print('НОЖНИЦЫ И ...')
    elif playerMove == 'б':
        print('БУМАГА И ...')

    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        computerMove = 'к'
        print('КАМЕНЬ \n')
    elif randomNumber == 2:
        computerMove = 'н'
        print('НОЖНИЦЫ \n')
    elif randomNumber == 3:
        computerMove = 'б'
        print('БУМАГА \n')

    if playerMove == computerMove:
        print('Ничья!\n')
        ties += 1
    elif playerMove == 'к' and computerMove == 'н':
        print('Победа\n')
        wins += 1
    elif playerMove == 'к' and computerMove == 'б':
        print('Поражение\n')
        losses += 1
    elif playerMove == 'н' and computerMove == 'б':
        print('Победа\n')
        wins += 1
    elif playerMove == 'н' and computerMove == 'к':
        print('Поражение\n')
        losses += 1
    elif playerMove == 'б' and computerMove == 'к':
        print('Победа\n')
        wins += 1
    elif playerMove == 'б' and computerMove == 'н':
        print('Поражение\n')
        losses += 1
