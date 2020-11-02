import random
from random import randint

lines=colomns=8
board=[[random.randrange(0,2,1) for i in range(colomns)] for j in range(lines)]

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
	

p1=str(input("what is the name of the player number 1? \n"))
p2=str(input("what is the name of the player number 2? \n"))
n=0
draw_board(board)

players_move=input('What is your move?\n')
while board.count([0]*lines)!=lines:
	n+=1
	delete(players_move, board, colomns, lines)
	draw_board(board)
	players_move=input('What is your move?\n')

if n%2==0:
	print(p2)
else:
	print(p1)	