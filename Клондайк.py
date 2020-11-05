def draw_board(board):
    for line in board:
        print(line)

board=[[0]*10 for i in range(10)]
ignore=[]
total=0

def checkInt(msg):
    for i in range(0,10):
        msg=msg.replace(str(i),"")
    return len(msg)==0

def inputXY():
    while True:
        x=input("X: ")
        y=input("Y: ")
        if not checkInt(x):
            print("Incorrect X")
            continue
        elif not checkInt(y):
            print("Incorrect Y")
            continue
        else:
            x=int(x)
            y=int(y)
            if x<1 or x>10:
                print("X out of range")
                continue
            if y<1 or y>10:
                print("Y out of range")
                continue
            if board[y-1][x-1]:
                print("Already filled")
                continue
            else:
                board[y-1][x-1]=True
            break
    return (y-1,x-1)

def inRange(x,y):
    if x<0:
        return False
    if y<0:
        return False
    if x>9:
        return False
    if y>9:
        return False
    return True

def border(x,y):
    dots=[]
    if inRange(x-1,y-1):
        dots+=[(x-1,y-1)]
    if inRange(x-1,y):
        dots+=[(x-1,y)]
    if inRange(x-1,y+1):
        dots+=[(x-1,y+1)]
    if inRange(x,y+1):
        dots+=[(x,y+1)]
    if inRange(x,y-1):
        dots+=[(x,y-1)]
    if inRange(x+1,y):
        dots+=[(x+1,y)]
    if inRange(x+1,y+1):
        dots+=[(x+1,y+1)]
    if inRange(x+1,y-1):
        dots+=[(x+1,y-1)]
    return dots

def contain(item, arr):
    for elem in arr:
        if elem[0]==item[0] and elem[1]==item[1]:
            return True
    return False

def check(x,y):
    global ignore
    global total
    global board
    ignore+=[(x,y)]
    if board[x][y]:
        total+=1
        for dot in border(x,y):
            if contain((dot[0],dot[1]),ignore):
                continue
            else:
                check(dot[0],dot[1])
    else:
        return total

while True:
    print("Game space:")
    draw_board(board)
    print("Enter coordinate:")
    (x,y)=inputXY()
    board[x][y]=1
    total=0
    ignore=[]
    check(x,y)
    if total>2:
        draw_board(board)
        print("You lost")
        break
    else:
        continue