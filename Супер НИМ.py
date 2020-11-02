import random
from random import randint

lines=colomns=8
board=[[random.randrange(0,2,1) for i in range(colomns)] for j in range(lines)] #создаём список с рандомно заполненными ячейками, 0 значит пустая, 1 значит есть фишка

#функция рисует доску
def draw_board(board):
	print('   1  2  3  4  5  6  7  8')
	print('A', board[0])
	print('B', board[1])
	print('C', board[2])
	print('D', board[3])
	print('E', board[4])
	print('F', board[5])
	print('G', board[6])
	print('H', board[7])

#функция удаляет строку или столбец введённый пользователем
def delete(players_move, board, colomns, lines):
	if players_move=='a':
		for i in range(colomns):
			board[0][i]=0
	elif players_move=='b':
		for i in range(colomns):
			board[1][i]=0
	elif players_move=='c':
		for i in range(colomns):
			board[2][i]=0
	elif players_move=='d':
		for i in range(colomns):
			board[3][i]=0
	elif players_move=='e':
		for i in range(colomns):
			board[4][i]=0
	elif players_move=='f':
		for i in range(colomns):
			board[5][i]=0
	elif players_move=='g':
		for i in range(colomns):
			board[6][i]=0
	elif players_move=='h':
		for i in range(colomns):
			board[7][i]=0
	else:
		players_move=int(players_move)
		for i in range(lines):
			board[i][players_move-1]=0
	

p1=str(input("what is the name of the player number 1? \n")) #запрос имени первого игрока
p2=str(input("what is the name of the player number 2? \n")) #запрос имени второго игрока
n=0
draw_board(board)          #рисуем доску

players_move=input('What is your move?\n')  #запрашиваем ход игрока
while board.count([0]*lines)!=lines:        #пока все элементы списка не будут состоять из одних нулей
	n+=1                                    #счётчик очерёдности хода
	delete(players_move, board, colomns, lines)  #удаляем фишки
	if board.count([0]*lines)==lines:             #заканчиваем не запрашиваем ничего и заканчиваем если больше нет фишек
		break    
	draw_board(board)                            #заново рисуем доску с изменёнными значениями               
	players_move=input('What is your move?\n')   #запрашиваем очередной ход игрока

if n%2==0:
	print(p2)
else:
	print(p1)	