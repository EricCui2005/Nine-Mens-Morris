import board
from point import opposing_team 
import random
import randomAI
import human_player

num_tests = 1000

num_white_wins = 0
num_black_wins = 0

for i in range(num_tests):

	#Play will begin with white (team = 1)
	team = 1
	
	#Play will begin at phase 1 (freely placing pieces until each team has placed 9 pieces)
	phase = 1
	
	#Initializing board object and randomAI to be utilized
	b = board.Board()
	randall = randomAI.randomAI()
	randy = randomAI.randomAI()
	
	
	#Initializing and printing an empty board
	
	"""Board printing is commented out for experiment purposes"""
	
	# print("Initial State")
	# b.print_board()
	
	#Returns a list of legal moves for phase 1 (simply unoccupied squares)
	valid_moves = b.p1_legal_moves()
	
	
	# Phase 1 Loop that executes until a phase change is detected
	while not b.phase_change():
	  
	  #Code chunk that allows the human player to play. The human plays as white (team = 1)
	  if team % 2 == 1:
	    randall.random_p1_move(team, b)
	
	  else:
	    randy.random_p1_move(team, b)
	
	
	  #Switches play to the opposing team
	  team = opposing_team(team)
	
	
	#Phase 2 is initiated when both teams have placed all of their resevoir pieces
	
	"""Informational printing is commented out for experiment purposes"""
		
	# print ("Phase 2 Beginning")
	  
	# Phase 2 While Loop 
	
	
	#Phase 2 terminates and the corresponding team wins when the opposing team has 2 or less pieces on the board or the opposing team has no more legal moves
	while not b.is_win_for_team(team):
	
	  #Code chunk allows the human player to make a move in phase 2. The human is still playing as white (team = 1)
		if team % 2 == 1:
			randall.random_p2_move(team, b)
		else:
			randy.random_p2_move(team, b)
	  #Checking if the most recent move caused a win condition
		if b.is_win_for_team(team):
			break
		team = opposing_team(team)
	
		"""Board printing is commented out for experiment purposes"""
		
		# b.print_board()
	
	print(f"Team {team} wins. Trial {i + 1}")

	if team == 1:
		num_white_wins += 1
	else:
		num_black_wins += 1

print(f"White Wins (Team 1): {num_white_wins}")
print(f"Black Wins (Team 2): {num_black_wins}")


    
  

