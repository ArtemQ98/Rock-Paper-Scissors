import random, sys

print('Добро пожаловать в "Камень, ножницы, бумага')
input('Нажмите любую клавишу, чтобы начать игру')

while True: #Цикл всей игры
    #Функция выбора игрока
    def choosePlayer(player_choose):

        if player_choose == 'к':
            return 'Камень против '
        elif player_choose == 'н':
            return 'Ножницы против '
        elif player_choose == 'б':
            return 'Бумага против '

#Выбор игрока
    listItem = ["к", "н", "б"]
    print('Камень - к, ножницы - н, бумага - б, выход - в')
    p = input('Введите ваш выбор: ')
    if p == 'в':
        print('Пока!')
        break
    else:
        randPlayer = choosePlayer(p)

    #Выбор компьютера
    def chooseComp(comp_choose):
        if comp_choose == 'к':
            return 'Камня'
        elif comp_choose == 'н':
            return 'Ножниц'
        elif comp_choose == 'б':
            return 'Бумаги'
    c = random.choice(listItem)
    randComp = chooseComp(c)

    print(randPlayer + randComp)

    wins = 0 #общая переменная побед
    losses = 0 #общая переменная поражений
    ties = 0 #общая переменная ничей

    #Условия игры и зачисления очков
    if p == c:
        print('Ничья!')
        ties += 1
    elif p == 'к' and c == 'б' or p == 'б' and c == 'н' or p == 'н' and c == 'к':
        print('Поражение!')
        losses += 1
    elif p == 'к' and c == 'н' or p == 'н' and c == 'б' or p == 'б' and c == 'к':
        print('Победа!')
        wins += 1
    else:
        print('none')
#результат
    print(str(wins) + ' Побед, ' + str(losses) + ' Поражений, ' + str(ties) + ' игр закончилось ничьёй.')
    print()