import board
from point import opposing_team 
from board_tester import quick_populate

# Run a game with the given functions for each turn
# If specified, start the game from a certain state
def play_game(team1_p1_move, team2_p1_move, team1_p2_move, team2_p2_move, quick_pop=None, MAX_TURNS=100):

	b = board.Board()
	
	#Initializing and printing an empty board
	print("Initial State")
	#b.print_board()
	
	#Initializing a board with the set up state
	if quick_pop is not None:
		t1_pieces, t2_pieces = quick_pop
		b = quick_populate(b, t1_pieces, t2_pieces)
	
	#Play will begin with white (team = 1)
	team = 1
	#Initializing board object and randomAI to be utilized
	b = board.Board()
	completed_turns = 0
	# Phase 1 Loop that executes until a phase change is detected
	while not b.phase_change():
		
		#Code chunk that allows the first player to play.
		if team % 2 == 1:
					   try:
							   team1_p1_move(team, b, completed_turns)
					   except ValueError:
							   break
		#Code chunk that allows the second player to play.
		else:
					   try:
							   team2_p1_move(team, b, completed_turns)
					   except ValueError:
							   break				
		#Switches play to the opposing team
		team = opposing_team(team)
		completed_turns += 1
	# Phase 2 is initiated when both teams 
	print ("Phase 2 Beginning")
		
	# Phase 2 While Loop 
	#b.print_board()
	
	#Phase 2 terminates and the corresponding team wins when the opposing team has 2 or less pieces on the board or the opposing team has no more legal moves
	while not b.is_win_for_team(team) and completed_turns < MAX_TURNS:
	
		#Code chunk allows the first player to make a move in phase 2. 
		if team % 2 == 1:
			team1_p2_move(team, b, completed_turns)
			
		
		else:
			if b.is_win_for_team(team):
				 break
			#Code chunk that allows the second player to play.
			team2_p2_move(team, b, completed_turns)
		#Checking if the most recent move caused a win condition
		if b.is_win_for_team(team):
			break
		
		team = opposing_team(team)
		completed_turns += 1

	
	#b.print_board()

	outcome = 0
	# Return the winner or stalemate depending on the outcome
	if b.is_win_for_team(team):
		outcome = team
	elif b.is_win_for_team(opposing_team(team)):
		outcome = opposing_team(team)
	# Return 3 if there is a stalemate
	elif completed_turns >= MAX_TURNS:
		outcome = 3
	piece_counts = [b.piece_counts(1), b.piece_counts(2)]
	return outcome, piece_counts
