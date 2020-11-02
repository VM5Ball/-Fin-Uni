#http://pythonicway.com/?catid=0&id=4
#индексы таблички
board = list(range(1,10))

#прорисовка таблицы
def draw_board(board):
    print ("-" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print ("-" * 13)

#учитывает ход игрока
def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("where to put " + player_token+"? ")   #запрашивает клеточку для хода игрока
        try:
            player_answer = int(player_answer)                       #берёт от него цифру
        except:
            print ("Wrong input, make sure you're entering a number") #если там число от 1 до 9
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer-1]) not in "XO"):             #проверяем что эта клетка не занята
                board[player_answer-1] = player_token
                valid = True
            else:
                print ("This box is already filled")                  #если занята, то сообщаем об этом
        else:
            print ("Wrong input. Write a number between 1 and 9.")   #если число не от 1 до 9

#функция проверяет что есть победная ситуация
def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))  #все возможные выигрышные варианты
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:                 #три победных ячейки равны, то есть х==х==х или о==о==о
            return board[each[0]]
    return False

#основная функция
def main(board):
    counter = 0           #счётчик для очерёдности хода
    win = False           #есть ли победа сейчас?
    while not win:        #пока нет победы
        draw_board(board) #рисуем таблицу
        if counter % 2 == 0:  #нечётный ход-ходит игрок крестиком
            take_input("X")
        else:
            take_input("O")   #чётный ход- ходит игрок ноликом
        counter += 1
        if counter > 4:       #как только ходов больше 4, то проверяем существует ли победная ситуация
            tmp = check_win(board)
            if tmp:               
                print (tmp, "Win!")
                win = True
                break
        if counter == 9:  #если победы нет, но 9 ходов сходили, то ничья
            print ("Draw!")
            break
    draw_board(board)

main(board)