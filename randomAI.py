# import board
# The quiet parameter in all of these functions controls whether or not the function outputs its outputs. If quiet is passed in as True, it will not print anything
from point import opposing_team 
import random

class randomAI:
	# Function to make a move in phase 1
	def random_p1_move(self, team, b):
		
		moves = b.p1_legal_moves()
		rn = random.randint(0, len(moves) - 1)
		move = moves[rn]
		r = int(move[0])
		p = int(move[1])
		b.p1_make_move(r, p ,team)
		
		# Evaluates if the newly placed piece creates a mill
		num_mills = b.mills_at(r, p, team)
  
    # Function to allow acting team to remove an opponent's piece using the (region, position) coordinate system
		for i in range(num_mills):
  
      # Code chunk makes use of the available_pieces_notation function to randomly remove one of the opposing team's pieces
			a_pieces = b.available_pieces_notation(opposing_team(team))
			rn = random.randint(0, len(a_pieces) - 1)
			ptbr = a_pieces[rn]
			tbr_r = int(ptbr[0])
			tbr_p = int(ptbr[1])
			b.remove_piece(tbr_r, tbr_p, team)
  
    
  # Function to make a move in phase 2. 
	def random_p2_move(self, team, b):
  
    # List to store legal moves at a certain position
		legal_moves = []
		
		# List with all points a certain team has pieces on
		a_pieces = b.available_pieces_notation(team)
		
		# While loop to ensure the randomAI only attempts to move a piece with 0 > legal moves
		while len(legal_moves) == 0:
			legal_moves = []
			while len(legal_moves) < 1:
				rnoo = random.randint(0, len(a_pieces) - 1)
				ptbm = a_pieces[rnoo]
				o_r = int(ptbm[0])
				o_p = int(ptbm[1])
				legal_moves = b.p2_legal_moves_notation(o_r, o_p)
  
    # Generating a random move after a valid piece at a position with 0 > legal moves has been selected by the while loop
			a_moves = b.p2_legal_moves_notation(o_r, o_p)
			
			rnom = random.randint(0, len(a_moves) - 1)
			rnm = a_moves[rnom]
			rm = int(rnm[0])
			pm = int(rnm[1])
			
			# Making the randomized phase 2 move and returning the "coordinates" of the move 
			b.p2_make_move(rm, pm, team, o_r, o_p)
    
		num_mills = b.mills_at(rm, pm, team)
		
		for i in range(num_mills):

      # Code chunk makes use of the available_pieces function to randomly remove one of the opposing team's pieces
			a_pieces = b.available_pieces_notation(opposing_team(team))
			rn = random.randint(0, len(a_pieces) - 1)
			ptbr = a_pieces[rn]
			tbr_r = int(ptbr[0])
			tbr_p = int(ptbr[1])
			
			b.remove_piece(tbr_r, tbr_p, team)

		return rm, pm
 