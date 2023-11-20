import point

class Player:
	# Takes in a board, the team that is currently taking a turn, and the phase of the game (1 or 2)
	def legal_turns(self, b, team, phase):
		# Return list of legal triplets : ([Origin], [Destination], [Removed]). 'Origin' describes where the piece is coming from (used for phase 2, this element will be empty for phase 1 moves). 'Destination' describes where the piece is going to be placed. 'Removed' describes which enemy piece will be removed should the destination element create a mill.

		# Loop through the origin positions
			# For each origin, loop through possible destinations
					# Check if there is a mill
						# If so, loop through all opponent pieces
					# Else give a triplet with an empty last spot

		# List to store the different legal turns
		l_turns = []

		# Temporary list to store triplet move information
		move = []

		# Code segment containing the logic for evaluating legal turns in phase 1 
		if phase == 1:

			# There is no destination for a piece in phase 1
			origin_ = None

			# Nested for loops to iterate through every position on the board
			for region in range(3):
				for position in range(8):
					
					move = []
					# Converts [region][position] into point notation
					notation_ = point.coordinates_to_notation(region, position)
					
					# Constructs a point object that will be appended to the [Destination] portion of the 'move' list
					dest = point.Point(team, notation_, region, position)

					# Following logic executes if the position being evaluated is unoccupied
					if b.full_board[region][position].occupied == 0:

						# Ignore multiple mills for the sake of simplification
						b.full_board[region][position].occupied = team
						if b.mills_at(region, position, team):

							# Iterates through the different pieces the opposing team has on the board and appends these different pieces to the 'Removed' portion of the 'move' turn triplet as well as the different pieces of collected information for 'Origin' and 'Destination'. This code chunk performs this generation for every move that would complete a mill
							for element in b.available_pieces(point.opposing_team(team)):

								# Make the turn based on the necessary information in the proper order ['Origin', 'Destination', 'Removed']
								move = [origin_, dest, element]

								# Appending the final move triplet to the l_turns list
								l_turns.append(move)

						else:

							# 'Removed' is set to 'None' if mills_at evaluates to false
							removed_ = None

							# Appending the necessary information in the proper order ['Origin', 'Destination', 'Removed']
							move = [origin_, dest, removed_]
							# Appending the final move triplet to the l_turns list
							l_turns.append(move)

						b.full_board[region][position].occupied = 0
			return l_turns

		# Code segment containing the logic for evaluating legal turns in phase 2 
		elif phase == 2:

			# Iterates through all of the available movable pieces a team has(even if the piece has no positions it can be moved to, in which case the 'Destination' portion of that moves triplet is set to none)
			for piece in b.available_pieces(team):

				# Iterates through all of the potential moves the piece being evaluated has 
				for potential_move in b.p2_legal_moves(piece.region, piece.position):
					# Checks if the potential_move creates a mill

					# Move the piece from the origin to the new position
					b.full_board[potential_move.region][potential_move.position].occupied = team
					b.full_board[piece.region][piece.position].occupied = 0
					if b.mills_at(potential_move.region, potential_move.position, team):
						# Iterates through all of the possible opposing pieces the team taking their turn can remove
						for opponent_piece in b.available_pieces(point.opposing_team(team)):

							# Appends the necessary information in the proper order ['Origin', 'Destination', 'Removed']
							move = [piece, potential_move, opponent_piece]

							# Appending the final move triplet to the l_turns list
							l_turns.append(move)

					else:
						
						# 'Removed' is set to 'None' if mills_at evaluates to false
						removed_ = None

						# Appending the necessary information in the proper order ['Origin', 'Destination', 'Removed']
						move = [piece, potential_move, removed_]

						# Appending the final move triplet to the l_turns list
						l_turns.append(move)
					# Move the piece back from the new position to the origin
					b.full_board[potential_move.region][potential_move.position].occupied = 0
					b.full_board[piece.region][piece.position].occupied = team

			return l_turns
			
	def make_p1_turn(self, turn, team, b, test = True):
		# Split turn triple into origin, move and removed
		origin, move, removed_ = turn

		# For p1, origin is not used. Instead place baced on move region and position
		b.p1_make_move(move.region, move.position, team, test)

		# If there is a piece to be removed, remove it
		if removed_:
			b.remove_piece(removed_.region, removed_.position, team)

		
	
	def undo_p1_turn(self, turn, team, b):
		# Split turn triple into origin, move and removed
		origin, move, removed_ = turn

		# The piece was placed at move, so return move to being an empty space
		b.full_board[move.region][move.position].occupied = 0
		# If there is a piece to be removed, remove it
		if removed_:
			b.full_board[removed_.region][removed_.position].occupied = point.opposing_team(team)
			
	def make_p2_turn(self, turn, team, b):
		# Split turn tuple into origin, move and removed

		origin, move, removed_ = turn

		# For p2 make move from origin to move position

		b.p2_make_move(move.region, move.position, team, origin.region, origin.position)


		# If there is a piece to be removed, remove it
		if removed_:
			b.remove_piece(removed_.region, removed_.position, team)

	def undo_p2_turn(self, turn, team, b):
		# Split turn triple into origin, move and removed
		origin, move, removed_ = turn
		
		# The piece was moved from origin, so return origin to being an piece for the team
		b.full_board[origin.region][origin.position].occupied = team
		
		# The piece was moved to move, so return move to being an empty space
		b.full_board[move.region][move.position].occupied = 0
		
		# If there is a piece to be removed, remove it
		if removed_:
			b.full_board[removed_.region][removed_.position].occupied = point.opposing_team(team)
	
	# Make a turn for a dynamic phase (calls either p1 or p2 function depending on argument)
	def make_turn(self, turn, team, b, phase, test=True):
		if phase == 1:
			self.make_p1_turn(turn, team, b, test)
		elif phase == 2:
			self.make_p2_turn(turn, team, b) 
			
	# Undo a turn that was run as a test for a dynamic phase
	def undo_turn(self, turn, team, b, phase):
		if phase == 1:
			self.undo_p1_turn(turn, team, b)
		elif phase == 2:
			self.undo_p2_turn(turn, team, b)