from point import opposing_team
# Class to store board scoring functions
class Scorers:
	# Simple board scorer of simply the team's number of pieces minus the opponent's number of pieces
	def simple_board_score(self, team, b, phase):
		return b.piece_counts(team) - b.piece_counts(opposing_team(team))

	def intermediate_board_score(self, team, b, phase):
		# Calculate board score based on the number of premills (2 team pieces and an empty space) and potential mills (1 team piece and two empty spaces) for both teams

		oppo = opposing_team(team)
		# Calculate pre mils and potential mills for each team
		num_team_premills = self.team_premills(team, b)
		num_team_potemills = self.team_potemills(team, b)
		num_oppo_premills = self.team_premills(oppo, b)
		num_oppo_potemills = self.team_potemills(oppo, b)
		piece_diff = b.piece_counts(team) - b.piece_counts(opposing_team(team)) 

		score = 0

		# Weights for each type of object
		PIECE_WEIGHT = 10
		PREMILL_WEIGHT = 3
		POTEMILL_WEIGHT = 2

		
		score += num_team_premills * PREMILL_WEIGHT
		score += num_team_potemills * POTEMILL_WEIGHT
		score += piece_diff * PIECE_WEIGHT
		score -= num_oppo_premills * PREMILL_WEIGHT
		score -= num_oppo_potemills * POTEMILL_WEIGHT
		return score
		
	def complex_board_score(self, team, b, phase):
		# Calculate board score based on the number of premills (2 team pieces and an empty space) and potential mills (1 team piece and two empty spaces) for both teams

		oppo = opposing_team(team)
		# Calcualte pre mils and potential mills for each team
		num_team_premills = self.team_premills(team, b)
		num_team_potemills = self.team_potemills(team, b)
		num_oppo_premills = self.team_premills(oppo, b)
		num_oppo_potemills = self.team_potemills(oppo, b)
		piece_diff = b.piece_counts(team) - b.piece_counts(opposing_team(team)) 

		#Difference in versatility
		vers_diff = self.piece_versatilities(team, b) - self.piece_versatilities(opposing_team(team), b)
		score = 0

		# Weights for each type of object
		PIECE_WEIGHT = 10
		PREMILL_WEIGHT = 3
		POTEMILL_WEIGHT = 2
		VERS_WEIGHT = 1

		# If it is phase 2, check if it is a win for any team. If it is set the score to a very large number
		if phase == 2:
			if b.is_win_for_team(team):
				score += 10000
			elif b.is_win_for_team(opposing_team(team)):
				score -= 10000
			
		
		score += num_team_premills * PREMILL_WEIGHT
		score += num_team_potemills * POTEMILL_WEIGHT
		score += piece_diff * PIECE_WEIGHT
		score -= num_oppo_premills * PREMILL_WEIGHT
		score -= num_oppo_potemills * POTEMILL_WEIGHT
		if phase == 1:
			score += vers_diff * VERS_WEIGHT
		return score
	
	def new_board_score(self, team, b, phase):
		# Calculate board score based on the number of premills (2 team pieces and an empty space) and potential mills (1 team piece and two empty spaces) for both teams

		oppo = opposing_team(team)
		# Calcualte pre mils and potential mills for each team
		num_team_premills = self.team_premills(team, b)
		num_team_potemills = self.team_potemills(team, b)
		num_oppo_premills = self.team_premills(oppo, b)
		num_oppo_potemills = self.team_potemills(oppo, b)
		

		#Difference in versatility
		vers_diff = self.piece_versatilities(team, b) - self.piece_versatilities(opposing_team(team), b)
		score = 0

		# Weights for each type of object
		PIECE_WEIGHT = 8
		PREMILL_WEIGHT = 3
		POTEMILL_WEIGHT = 2
		VERS_WEIGHT = 1

		# If it is phase 2, check if it is a win for any team. If it is set the score to a very large number
		if phase == 2:
			if b.is_win_for_team(team):
				return 10000
			elif b.is_win_for_team(opposing_team(team)):
				return -10000
			
		
		score += num_team_premills * PREMILL_WEIGHT
		score += num_team_potemills * POTEMILL_WEIGHT
		score += b.piece_counts(team)  * PIECE_WEIGHT
		score -= 5 * PIECE_WEIGHT * b.piece_counts(opposing_team(team)) 
		score -= num_oppo_premills * PREMILL_WEIGHT
		score -= num_oppo_potemills * POTEMILL_WEIGHT
		if phase == 1:
			score += vers_diff * VERS_WEIGHT
		return score
	
	
	def piece_versatilities(self, team, b):
		total = 0
		for piece in b.available_pieces(team):
			total += len(b.p2_legal_moves(piece.region, piece.position))
		return total
		
	def team_premills(self, team, b):
		total = 0
		for piece in b.available_pieces(team):
			mills = self.premills_at(piece.region, piece.position, team, b)
			total += len(mills)
	
		# Each premill is counted twice because there are two same pieces in each premill. Thus premills_at will be valid for two pieces
		return round(total/2, 0)

	# Counts the number of potential mills for a team. 
	def team_potemills(self, team, b):
		total = 0
		for piece in b.available_pieces(team):
			total += self.potential_premill_count_at(piece.region, piece.position, b)
		return total
			
	def premills_at(self, region, position, team, b):
		# Even case (can make mills going clockwise in the same region or counterclockwise in the same region)
		if position % 2 == 0:
			
			# Gets points located "+1" and "+2" (clockwise) of the testing position and appends them to the appropriate list
			pf_1 = b.full_board[region][(position + 1) % 8]
			pf_2 = b.full_board[region][(position + 2) % 8]
	 
			
			# Gets points located "-1" and "-2" (counterclockwise) of the testing position and appends them to the appropriate list
			pb_1 = b.full_board[region][(position - 1) % 8]
			pb_2 = b.full_board[region][(position - 2) % 8]
			
	
			# Evaluates if any of the two points counterclockwise or clockwise is occupied by the same piece. If it is, we can assume that the other point in the same direction is unoccupied (because mills_at is 0) and will complete a mill
			pieces = []
					
			# print(f"here for {region}, {position}, team {team}, which is even")
			if pf_1.occupied == team and pf_2.occupied == 0:
				pieces.append(pf_2)
			elif pf_2.occupied == team and pf_1.occupied == 0:
				pieces.append(pf_1)

			# Back Mill
			if pb_1.occupied == team and pb_2.occupied == 0:
				pieces.append(pb_2)
			elif pb_2.occupied == team and pb_1.occupied == 0:
				pieces.append(pb_1)
									
			return pieces
					
			
			
		else:
				# print(f"here for {region}, {position}, team {team}, which is odd")
				# Points one clockwise and one counterclockwise of the testing position
				pf_1 = b.full_board[region][(position + 1) % 8]
				pb_1 = b.full_board[region][(position - 1) % 8]
				# print("pf_1 occ: ", pf_1.occupied, " pb_1 occ: ", pb_1.occupied)
		
				# # Points in the same position as the testing point (including the testing position for convenience)
				# p0 = b.full_board[0][p.position]
				# p1 = b.full_board[1][p.position]
				# p2 = b.full_board[2][p.position]
		
				pieces = []

				if pf_1.occupied == team and pb_1.occupied == 0:
					pieces.append(pb_1)
				elif pb_1.occupied == team and pf_1.occupied == 0:
					pieces.append(pf_1)
	
				# [Unoccupied], [Team], [Opposing Team]
				piece_states = [[], [], []]
				
				for i in range(3):
					piece = b.full_board[i][position]
					# Check if the piece's state is empty, same team, or opposite:
					if piece.occupied == 0:
						piece_states[0].append(piece)
					elif piece.occupied == team:
						piece_states[1].append(piece)
					elif piece.occupied == opposing_team(team):
						piece_states[2].append(piece)
			
					#check if length of team list is 2, length of empty is 1; add piece 
					if len(piece_states[0]) == 1 and len(piece_states[1]) == 2 and len(piece_states[2]) == 0:
						pieces.append(piece_states[0][0])
				
				return pieces 
		
	
	
	
	
	
	##If the piece has two open spaces in its row or column, add to count
	# Return the count
	def potential_premill_count_at(self, region, position, b):
		#array to return
		empty_spaces = []
		p = b.full_board[region][position]
		
		#Points located "+1" and "+2" (clockwise) of the testing position
		pf_1 = b.full_board[region][(position + 1) % 8]
		pf_2 = b.full_board[region][(position + 2) % 8]
	
		#Points located "-1" and "-2" (counterclockwise) of the testing position
		pb_1 = b.full_board[region][(position - 1) % 8]
		pb_2 = b.full_board[region][(position - 2) % 8]
	
		total = 0
		
		#Even Case (0 = not in a mill, 1 = in one mill, 2 = in two mills)
		if position % 2 == 0:
			
				# Empty spaces going forward
				if (pf_1.occupied == 0) and (pf_2.occupied == 0):
						total += 1
					
				# Empty spaces going backward
				if (pb_1.occupied == 0) and (pb_2.occupied == 0):
						total += 1
				return total
	
		else:
				# Empty spaces going horizontally
				if (pf_1.occupied == 0) and	(pb_1.occupied == 0):
						total += 1
					
				# Empty spaces for mills that cross the region
				p1 = b.full_board[(region+1)%3][position]
				p2 = b.full_board[(region+2)%3][position]
				if (p1.occupied == 0) and (p2.occupied == 0):
						total += 1
	
				return total



"""To shorten runtime of algorithm:
When iterating through pieces and determining if they are in a premill, remove the pieces that are in a premill from the list of available pieces that is iterated through in the potemills function"""