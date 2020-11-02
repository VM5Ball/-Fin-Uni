from itertools import *

board = list(range(1,21))
board=list(map(str, board))


#функция прорисовка таблицы
def draw_board(board):
	print ("-" * 26)
	for i in range(20):
		if len(board[i])==1:           #если один символ то есть пробел перед палочокой
			print ("|", board[i], ' ', end='')
		if len(board[i])==2:           #если два символа то нет пробела
			print ("|", board[i]+' ', end='')
		if i==4 or i==9 or i==14 or i==19:    #новая строка после ячеек 5 10 15
			print('\n')
	print ("-" * 26)


#функция берёт число которое вводит игрок и проверяет подходит ли оно, если да, то вносит в таблицу
def take_input():
	valid = False
	while not valid:
		player_answer = input("where to put " + token[ochered]+"? ")  #запрашивает клеточку для хода игрока
		try:
			player_answer = int(player_answer)                       #берёт от него цифру
		except:
			print ("Wrong input, make sure you're entering a number") #если там не число
			continue
		if player_answer >= 1 and player_answer <= 20:
			if (str(board[player_answer-1]) not in "xoz"):             #проверяем что эта клетка не занята
				board[player_answer-1] = token[ochered]
				valid = True
			else:
				print ("This box is already filled")                  #если занята, то сообщаем об этом
		else:
			print ("Wrong input. Write a number between 1 and 20.")  #если число не от 1 до 20

def count_mistakes():
	#все пары, за которые плюс очко
	pairs=((0,1), (0,5), (0,6), (1,2), (1,5), (1,6), (1,7), (2,3), (2,7), (2,8), (2,6), (3,4), (3,8), (3,9), (3,7), (4,8), (4,9), (5,6), (5,11), (5,10), (6,10), (6,11), (6,12), (6,7), (7,11), (7,12), (7,13), (7,8), (8,12), (8,13), (8,14), (8,9), (9,13), (9,14), (10,15), (10,16), (10,11), (11,15), (11,16), (11,17), (11,12), (12,16), (12,17), (12,18), (12,13), (13,17), (13,18), (13,19), (13,14), (14,18), (14,19), (15,16), (16,17), (17,18), (18,19))
	for each in pairs:
		if board[each[0]] == board[each[1]]:         #если заполненая ячейка равна соседу, то плюс один в счётчик
			counter[0 if board[each[0]]=='x' else (1 if board[each[0]]=='o' else 2)]+=1
    


draw_board(board)

p1=str(input('Name player 1, token = x \n'))
p2=str(input('Name player 2, token = o \n'))
p3=str(input('Name player 3, token = z \n'))

token=['x', 'o', 'z']  #токены игроков
ochered=0  #счётчик очереди
counter=[0,0,0]  #счётчик пар

for i in range(20):   
	take_input()
	draw_board(board)
	ochered+=1
	if ochered==3:
		ochered=0

count_mistakes()

print('Player', p1, 'has', counter[0], "mistakes")
print('Player', p2, 'has', counter[1], "mistakes")   
print('Player', p3, 'has', counter[2], "mistakes")
winner_amount=min(counter)  #минимальное количество ошибок среди игроков
print('Winners are:')
if counter[0]==winner_amount:
	print(p1)
if counter[1]==winner_amount:
	print(p2)
if counter[2]==winner_amount:
	print(p3)