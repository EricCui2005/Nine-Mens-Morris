import board 
import random as rd
from point import *

class Greedy:
	# Function that takes in a board and a team and returns the most favorable move in notation format
	def get_premills(self, b, team):
		complete_mill = []
		for element in b.available_pieces(team):
			spaces = self.premills_at(element.region, element.position, team, b)
			b.mills_at(element.region, element.position, team)
			if spaces is not None:	
				nots = [space.notation for space in spaces]
				print(f"{nots} complete mill at position {element.notation}")
				complete_mill.extend(spaces)
		return complete_mill
		
	def greedy_p1_move(self, b, team):

		# Completing a friendly mill
		
		complete_mill = self.get_premills(b, team)
				
		# # Block enemy premill
		# block_enemy = self.get_premills(b, opposing_team(team))

		# # Making a premill
		# make_premill = []
		# for element in b.available_pieces(team):
		# 	make_premill.extend(self.potential_premill(element.region, element.position, b))
			
		
		# Versatility
		versatilities = []

		#Calculate Versatilities of available elements 
		for element in b.available_pieces(0):
			versatility = self.pt_versatility(element.region, element.position, b)
			versatilities.append((element, versatility))
		#Sort piece order by versatility
		versatilities.sort(key=lambda a: a[1], reverse = True)

		#Extract pieces from pair of (piece, versatiltiy)
		vers_elements = [piece for piece, versatility in versatilities]

		if len(complete_mill) != 0:
			decider = rd.randint(0, len(complete_mill) - 1)
			print("Complete mill:", complete_mill)
			g_move = complete_mill[decider]
			b.p1_make_move(g_move.region, g_move.position, team)
		# elif len(block_enemy) != 0:
		# 	decider = rd.randint(0, len(block_enemy) - 1)
		# 	g_move = block_enemy[decider]
		# 	print(g_move)
		# 	b.p1_make_move(g_move.region, g_move.position, team)
		# elif len(make_premill) != 0:
		# 	decider = rd.randint(0, len(make_premill) - 1)
		# 	g_move = make_premill[decider]
		# 	b.p1_make_move(g_move.region, g_move.position, team)
		elif len(versatilities) != 0:
			# decider = rd.randint(0, len(versatilities))
			point = versatilities[0][0]
			b.p1_make_move(point.region, point.position, team)
		else:
			# raise "uh oh, ran out of moves"
			print("what the")

		print(versatilities)
		return


 # Takes in a certain point. The function evaluates if the point is a part of a premill (defined to be a linear sequence of three positions with two regions occupied by the same team and one unoccupied position). If the point is evaluated to be part of a premill, the function will return a list of points that, should it become occupied by a piece from the same team, will complete the mill
	def premills_at(self, region, position, team, b):
	
		# Even case (can make mills going clockwise in the same region or counterclockwise in the same region)
		if position % 2 == 0:
			total = 0
			
			# Gets points located "+1" and "+2" (clockwise) of the testing position and appends them to the appropriate list
			pf_1 = b.full_board[region][(position + 1) % 8]
			pf_2 = b.full_board[region][(position + 2) % 8]
	 
			
			# Gets points located "-1" and "-2" (counterclockwise) of the testing position and appends them to the appropriate list
			pb_1 = b.full_board[region][(position - 1) % 8]
			pb_2 = b.full_board[region][(position - 2) % 8]
			
			b = board.Board()
	
			# Evaluates if any of the two points counterclockwise or clockwise is occupied by the same piece. If it is, we can assume that the other point in the same direction is unoccupied (because mills_at is 0) and will complete a mill
			pieces = []
					
			if b.mills_at(region, position, team) == 0:
				print(f"here for {region}, {position}, team {team}")
				if pf_1.occupied == team:
					pieces.append(pf_2)
				elif pf_2.occupied == team:
					pieces.append(pf_1)
	
							#Back Mill
				if pb_1.occupied == team:
					pieces.append(pb_2)
				elif pb_2.occupied == team:
					pieces.append(pb_1)
									
				return pieces
					
			else:
		
				# Points one clockwise and one counterclockwise of the testing position
				pf_1 = b.full_board[region][(position + 1) % 8]
				pb_1 = b.full_board[region][(position - 1) % 8]
		
				# # Points in the same position as the testing point (including the testing position for convenience)
				# p0 = b.full_board[0][p.position]
				# p1 = b.full_board[1][p.position]
				# p2 = b.full_board[2][p.position]
		
				pieces = []
				if b.mills_at(region, position, team) == 0:
					if pf_1.occupied == team:
						return pieces.append(pb_1)
					elif pb_1.occupied == team:
						return pieces.append(pf_1)
		
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
				
		
	#literally just the check for mill func but checks for 2 open spaces in the column/row
	##If the piece has two open spaces in its row or column, return those empty spaces.
	def potential_premill(self, region,position, b):
		#array to return
		empty_spaces = []
		p = b.full_board[region][position]
		
		#Points located "+1" and "+2" (clockwise) of the testing position
		pf_1 = b.full_board[region][(position + 1) % 8]
		pf_2 = b.full_board[region][(position + 2) % 8]
	
		#Points located "-1" and "-2" (counterclockwise) of the testing position
		pb_1 = b.full_board[region][(position - 1) % 8]
		pb_2 = b.full_board[region][(position - 2) % 8]
	
		#Even Case (0 = not in a mill, 1 = in one mill, 2 = in two mills)
		if position % 2 == 0:
				# Empty spaces going forward
				if not pf_1 and not pf_2:
						empty_spaces.append(pf_1)
						empty_spaces.append(pf_2)
					
				# Empty spaces going backward
				if not pb_1 and not pb_2:
						empty_spaces.append(pb_1)
						empty_spaces.append(pb_2)
	
				return empty_spaces
	
		else:
				# Empty spaces going horizontally
				if (not pf_1) and	(not pb_1):
						empty_spaces.append(pf_1)
						empty_spaces.append(pb_1)
					
				# Empty spaces going vertically
				p1 = b.full_board[(region+1)%3][position]
				p2 = b.full_board[(region+2)%3][position]
				if (not p1) and (not p2):
						empty_spaces.append(p1)
						empty_spaces.append(p2)
	
				return empty_spaces
	
	
	#calculates the versatility of a given point
	#higher return value means better versatility
	def pt_versatility(self, region, position, b):
	
			#sets a variable to store the versatility of an empty space
			#higher value means less versatility
			value = 0
	
			#check whether the position in front or behind the space is occupied and increase value accordingly
			if b.full_board[region][(position + 1) % 8].occupied == 0:
					value += 1
			if b.full_board[region][(position-1) % 8].occupied == 0:
					value += 1
	
			#check whether the chosen space is at an odd position
			if position % 2 == 1:
					#if the chosen space is in region 0 or 1, check if the space in the next region is occupied and increase value accordingly
					if region == 0 or region == 1:
							if b.full_board[region+1][position].occupied == 0:
									value += 1
					#if the chosen space is in region 1 or 2, check if the space in the previous region is occupied and increase value accordingly
					if region == 1 or region == 2:
							if b.full_board[region-1][position].occupied == 0:
									value += 1
	
			return value
	
	#returns the point with the best versatility given a list of potential points
	def best_versatility(self, pts_list):
	
			#set best to 0
			best = 0
	
			#loop through the list of versatility values
			for element in pts_list:
					#if a value is greater than the value for best, reassign best to the new value
					if element > best:
							best = element
	
			return best
	
	
	#returns the best piece to remove from an enemy mill. Best point to remove is deemed to be the piece with the most versatility - team given is enemy team
	def find_millpiece_to_remove(self, region, position, team, b):
	
		#Temporary variable to store the information for the position being evaluated
		p = b.full_board[region][position]
		#store versatility for p
		p_versatility = self.point_versatility(p)
	
		#P is not the same team
		if p.occupied != team:
			#Should not happen
			raise "Wrong team error"
			return 0

		#Points located "+1" and "+2" (clockwise) of the testing position
		pf_1 = b.full_board[region][(p.position + 1) % 8]
		pf_2 = b.full_board[region][(p.position + 2) % 8]

		#Points located "-1" and "-2" (counterclockwise) of the testing position
		pb_1 = b.full_board[region][(p.position - 1) % 8]
		pb_2 = b.full_board[region][(p.position - 2) % 8]

		total = 0

		#stores versatility for each point
		pf1_versatility = self.point_versatility(pf_1)
		pf2_versatility = self.point_versatility(pf_2)
		pb1_versatility = self.point_versatility(pb_1)
		pb2_versatility = self.point_versatility(pb_1)

		#creates a list to store the points and their respective versatilities
		list = [[p, p_versatility]]

		
		#Even Case (0 = not in a mill, 1 = in one mill, 2 = in two mills)
		if position % 2 == 0:
			# Mill going forward
			if same_team(p, pf_1) and same_team(p, pf_2):
				#appends points in the mill and their versatilities to the list
				list.append([pf_1, pf1_versatility])
				list.append([pf_2, pf2_versatility])
			# Mill going backward
			if same_team(p, pb_1) and same_team(p, pb_2):
				#appends points in the mill and their versatilities to the list
				list.append([pb_1, pb1_versatility])
				list.append([pb_2, pb2_versatility])

		else:
			# Mill going horizontally
			if same_team(p, pf_1) and same_team(p, pb_1):
				#appends points in the mill and their versatilities to the list
				list.append([pf_1, pf1_versatility])
				list.append([pb_1, pb1_versatility])
				
			# Mill going vertically
			p0 = b.full_board[0][p.position]
			p1 = b.full_board[1][p.position]
			p2 = b.full_board[2][p.position]

			#stores the versatilities of each point
			p0_versatility = point_versatility(p0)
			p1_versatility = point_versatility(p1)
			p2_versatility = point_versatility(p2)
			
			if same_team(p0, p1) and same_team(p1, p2):
				#appends points in the mill and their versatilities to the list
				list.append([p0, p0_versatility])
				list.append([p1, p1_versatility])
				list.append([p2, p2_versatility])

		#create a variable to store the best versatility value
		best = 0

		for element in list:
			#check if the current element has a higher versatility than best
			if element[1] > best:
				#reassign best and best_point
				best = element[1]
				best_point = element[0]

		return best_point
								
								

	
	
	
	
	##If the piece has an ally piece and an enemy piece in its row or column, return the enemy piece.
	def unblock_premill(self, region,position, b):
		#array to return
		blocking_spaces=[]
		p=b.full_board[region][position]
		
		#Points located "+1" and "+2" (clockwise) of the testing position
		pf_1 = b.full_board[region][(p.position + 1) % 8]
		pf_2 = b.full_board[region][(p.position + 2) % 8]
	
		#Points located "-1" and "-2" (counterclockwise) of the testing position
		pb_1 = b.full_board[region][(p.position - 1) % 8]
		pb_2 = b.full_board[region][(p.position - 2) % 8]
	
		#Even Case (0 = not in a mill, 1 = in one mill, 2 = in two mills)
		if position % 2 == 0:
	
				# Consider a refactor?
			
				# Empty spaces going forward
				if (pf_1==p.team and pf_2!=0 and pf_2!=p.team):
					blocking_spaces.append(pf_2)
					
				elif pf_2 == p.team and pf_1 !=0 and pf_1 != p.team:
					blocking_spaces.append(pf_1)
	
					
				# Empty spaces going backward
				if (pb_1==p.team and pb_2!=0 and pb_2!=p.team):
					blocking_spaces.append(pb_2)
					
				elif (pb_2 == p.team) and (pb_1 != 0) and (pb_1 != p.team):
					blocking_spaces.append(pb_1)
	
				return blocking_spaces
	
		else:
				# Empty spaces going horizontally
				if (pf_1 == p.team) and (pb_1 != 0) and (pb_1 != p.team):
					blocking_spaces.append(pb_1)
					
				elif (pb_1 == p.team) and (pf_1 != 0) and (pf_1 != p.team):
					blocking_spaces.append(pf_1)
					
				# Empty spaces going vertically
				p1 = b.full_board[(region+1)%3][p.position]
				p2 = b.full_board[(region+2)%3][p.position]
			
				if (p1 == p.team) and (p2 != 0) and (p2 != p.team):
					blocking_spaces.append(p2)
					
				elif(p2 == p.team) and (p1 != 0) and (p1 != p.team):
					blocking_spaces.append(p1)
	
				return blocking_spaces

	#given a space on the board, determine a list of pieces that are eligible to move into the given space
	def can_move_to(self, space, team):

		#initialize a list to store the options
		list = []

		#set variables for te pieces in the position ahead and behind of the space
		pf = self.full_board[space.region][(space.position + 1) % 8]
		pb = self.full_board[space.region][(space.position - 1) % 8]

		#check if the variables are on the same team as the space and append them to the list if they are
		if same_team(space, pf):
			list.append(pf)
		if same_team(space, pb):
			lsit.append(pb)

		#if the space is in an odd position, check the adjacent regions
		if space.position % 2 == 1:
			#if the region is 0 or 1, look at the piece in the next region
			if space.region == 0 or space.region == 1:
				rf = self.full_board[space.region + 1][space.position]
				#check if the piece in the next region is of the same team as the space and append it to the list
				if same_team(space, rf):
					list.append(pf)
			#if the region is 1 or 2, look at the piece in the previous region
			if space.region == 1 or space.region == 2:
				rb = self.full_board[space.region - 1][space.position]
				#check if the piece in the previous region is of the same team and append it to the list if it is
				if same_team(space, rb):
					list.append(pb)
		#return the list of possible pieces to move into the given space
		return list
			
	
	def mill_completion(self, b, team):
		spaces = self.get_premills(b, team)
		for space in spaces:
			options = self.can_move_to(space)
			self.check_options(options, space)



  #given a list of possible pieces to move into a given space, iterate throught the list and check if moving said piece into the given space would result in a mill or if it would remain an incomplete mill
  #then return which piece would result in the creation of a mill if moved into the given space
	def check_options(self, options, space, b):

		#initialize a list to keep eligible pieces
		list = []
		#iterate through given list of options
		for option in options:

			#store piece's original region and position
			origin_region = option.region
			origin_position = option.position
			#move the current piece to the parameter space
			b.p2_make_move(self, space.region, space.position, option.team, option.region, option.position)
			#check if there is now a mill at the given space and append the piece to our list if does make a mill
			if b.mills_at(self, space.region, space.position, option.team) > 0:
				list.append(option)

			#move the piece back to its original position so as to not mess up the board
			b.p2_make_move(self, origin_region, origin_position, option.team, space.region, space.position)

		#return a piece that makes a mill
		return list

	def greedy_p2_move(self, b, team):
		pass
		
			
		
	
