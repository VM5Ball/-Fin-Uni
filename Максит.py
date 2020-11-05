import random
from random import randint

lines=colomns=3
board=[[random.randrange(1,9) for i in range(colomns)] for j in range(lines)]
counter=[0,0]
n=0

def draw_board():
	for el in board:
		print(el)

def take_input1(n):
	flag=False
	while not flag:
		x=input('Enter colomn: ')
		y=input('Enter row: ')
		try:
			x = int(x)
			y = int(y)
		except:
			print ("Wrong input, make sure you're entering a number") 
			continue
		if x >= 1 and x <= 3 and y>=1 and y<=3:
			if (str(board[y-1][x-1]) in "123456789"):
				
				flag = True
			else:
				print ("This box is already empty")
		else:
			print ("Wrong input. Write numbers between 1 and 3.") 
	return (y-1,x-1)
'''
def take_input(n, last_move):
	flag=False
	while not flag:
		x=input('Enter colomn: ')
		y=input('Enter row: ')
		try:
			x = int(x)
			y = int(y)
		except:
			print ("Wrong input, make sure you're entering a number") 
			continue
		if x >= 1 and x <= 3 and y>=1 and y<=3:
			if (str(board[y-1][x-1]) in "123456789"):
				
				flag = True
			else:
				print ("This box is already empty")
		else:
			print ("Wrong input. Write numbers between 1 and 3.") 
	return (y-1,x-1)

'''
def delete(players_move):
	counter[n%2]+=board[players_move[0]][players_move[1]]
	board[players_move[0]][players_move[1]] = 0


p1=str(input("what is the name of the player number 1? \n")) #запрос имени первого игрока
p2=str(input("what is the name of the player number 2? \n")) #запрос имени второго игрока
while board.count([0]*lines)!=lines:
	draw_board()
	players_move=take_input1(n)
	delete(players_move)
	#last_move=players_move
	n+=1

print('Player', p1, 'has', counter[0], "points")
print('Player', p2, 'has', counter[1], "points")
