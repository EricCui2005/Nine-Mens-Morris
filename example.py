# Example code from Prof. Simonnetti
import copy
import random

def clearboard(board): # puts a space into every spot on the board
	for r in range(0,8): # the list [0,1,2]
		board[r] = [" "," "," "," "," "," "," "," "]

def flipboard(board): # turns every X to an O and every O to an X
	for r in range(0,8):
		for c in range(0,8):
			if board[r][c]=="O": # use double equal for comparison
				board[r][c]="X"	 # use single equal for assignment
			elif board[r][c]=="X":
				board[r][c]="O"

def printboard(board): # prints the board to the screen
	print ("\n\n\n\n\n\n\n   1   2   3   4   5   6   7   8")
	for r in range(0,8):
		if r>0:
			print ("  ---+---+---+---+---+---+---+---") 
		for c in range(0,8):
			if c>0:
				print(" | ",end="")
			else:
				print(chr(65+r),end="  ")
			print(board[r][c],end="")
		print()
	print()
    
def checkDir(board,x,y,tok,dx,dy): # return zero if nothing should be flipped, or return the number of items to be flipped in this direction
    count = 1
    x = x+dx
    y = y+dy
    opp = "O" if tok == "X" else "X"
    if (x>-1 and x<8 and y>-1 and y<8 and board[y][x]==opp):
        x = x+dx
        y = y+dy
        while (x>-1 and x<8 and y>-1 and y<8 and board[y][x]==opp):
            x = x+dx
            y = y+dy
            count = count+1
        if (x>-1 and x<8 and y>-1 and y<8 and board[y][x]==tok):
            return(count)
    return(0)

def makemove(board,token,spot): # places the token on the board at a certain spot
    board[spot[0]][spot[1]] = token
    for i in range(0,3):
        print(i)
        for j in range (0,3):
            if (i!=1 or j!=1):
                n = checkDir(board,spot[1],spot[0],token,i-1,j-1)
                tX = spot[1]
                tY = spot[0]
                for k in range(0,n):
                    tX=tX+i-1
                    tY=tY+j-1
                    board[tY][tX] = token
	
def legalmoves(board,tok): # returns a list of legal moves
	legals = []
	for r in range(0,8):
		for c in range(0,8):
			if (board[r][c] == " " and (checkDir(board,c,r,tok,-1,-1) 
                                  or checkDir(board,c,r,tok,-1,0) 
                                  or checkDir(board,c,r,tok,-1,1) 
                                  or checkDir(board,c,r,tok,0,-1) 
                                  or checkDir(board,c,r,tok,0,1) 
                                  or checkDir(board,c,r,tok,1,-1) 
                                  or checkDir(board,c,r,tok,1,0) 
                                  or checkDir(board,c,r,tok,1,1))):
				legals.append([r,c])
	return legals

def checkwin(board,spot): # check to see if move at spot creates a win
#	r = spot[0] # row of last move
#	c = spot[1] # column of last move
#	if board[r][0] == board[r][1] and board[r][0] == board[r][2]:
#		return (True) # horizontal win
#	if board[0][c] == board[1][c] and board[0][c] == board[2][c]:
#		return (True) # vertical win
#	if r==c and board[0][0]==board[1][1] and board[0][0]==board[2][2]:
#		return (True) # main diagonal win
#	if r+c==2 and board[0][2]==board[1][1] and board[0][2]==board[2][0]:
#		return (True) # off diagonal win
	return (False)

#def humanturn(board,token): # returns a move made by a human
#	while True:
#		inp = input("Player "+token+", where would you like to move? ")
#		r = ord(inp[0])%32 - 1
#		c = int(inp[1]) - 1
#		if c>2 or c<0 or r>2 or r<0 or board[r][c]!=" ":
#			print("Not a legal move, try again.")
#		else:
#			return ([r,c])

def randomturn(board,tok): # returns a random legal move
	return random.choice(legalmoves(theBoard,tok))
	
#def calcboard(board,spot): # returns a numeric value for a board (X point of view)
#	if checkwin(board,spot):
#		return 100
#	boardval = 0
#	for r in range(0,3):
#		for c in range(0,3):
#			if board[r][c] == "X":
#				mult = 1
#			elif board[r][c] == "O":
#				mult = -1
#			else:
#				mult = 0
#			if r==1 and c==1:
#				spotval = 3 # middle
#			elif r-c == 1 or c-r == 1:
#				spotval = 1 # side
#			else:
#				spotval = 2 # corner
#			boardval = boardval + mult*spotval
#	return boardval

def lookahead(board,level,lastmove): # returns the best value for any possible move
	if level==0:
		return calcboard(board,lastmove)
	else:
		movelist = legalmoves(board,"X")
		bestval = -998
		for mymove in movelist:
			tempBoard = copy.deepcopy(board)
			flipboard(tempBoard)
			makemove(tempBoard,"X",mymove)
			if checkwin(tempBoard,mymove):
				return (-1000)
			val = lookahead(tempBoard,level-1,mymove)
			if val > bestval:
				bestval = val
		return (-bestval)
		
def smartturn(board,level,token): # returns best legal move
	movelist = legalmoves(board,"X")
	random.shuffle(movelist)
	bestval = -1001
	bestmove = []
	for mymove in movelist:
		tempBoard = copy.deepcopy(board)
		if token=="O":
			flipboard(tempBoard)
		makemove(tempBoard,"X",mymove)
		if checkwin(tempBoard,mymove):
			return (mymove)
#		val = calcboard(tempBoard,mymove)
		val = lookahead(tempBoard,level,mymove)
		if val > bestval:
			bestval = val
			bestmove = copy.copy(mymove)
#	print ("bestval is ",bestval)
	return (bestmove)

Pause = True	
theBoard=[[],[],[],[],[],[],[],[]]
clearboard(theBoard)
theBoard[4][4]=theBoard[3][3]="X"
theBoard[3][4]=theBoard[4][3]="O"
#theBoard[3][4]="X"
gameover = False
who = "X"
where = []
playerDictionary = {"X":"random","O":"random"}
printboard(theBoard)
print(legalmoves(theBoard,"X"))
while not gameover:
	if playerDictionary[who] == "human":
		where = humanturn(theBoard,who)
	elif playerDictionary[who] == "random":
		where = randomturn(theBoard,who)
	elif playerDictionary[who] == "smart":
		where = smartturn(theBoard,2,who)
	else:
		print("I'm confused.")
		break;
	makemove(theBoard,who,where)
	printboard(theBoard)
	if checkwin(theBoard,where):
		gameover = True
		print("Congratulations,",who+", you are the winner!")
	elif legalmoves(theBoard,who) == []:
		gameover = True
		print("The game is a draw.")
	if who=="X":
		who = "O"
	else:
		who = "X"
	if Pause:
		input("Press Enter to Continue")
print("Thank you for playing.")
print("Your credit card has been charged 99 cents.")
		

