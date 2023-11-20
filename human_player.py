# import board
from point import opposing_team, coordinates_to_notation, notation_to_coordinates 
import random
import board_tester as bt


  
class human_player:
  def input_position(self, l_m):
    r, p = 0, -1
    remove = ""
    while not remove in l_m:
      r = int(input("Enter region: "))
      p = int(input("Enter position: "))
      remove = str(r) + str(p)
    return r, p
    
  def use_mills(self, num_mills, team, b):
    for i in range(num_mills):
      print("Remove an Opposing Piece")
      b.print_board()
      #Code chunk makes use of the available_pieces function to randomly remove one of the opposing team's pieces
      legal_moves = b.available_pieces_notation(opposing_team(team))

      r, p = self.input_position(legal_moves)
      remove = str(r) + str(p)

      b.remove_piece(r, p, team)
      print(f"Team {opposing_team(team)}'s piece removed at {remove}")
    

  def make_p1_move(self, team, b):
    
    legal_moves = b.p1_legal_moves()
    print(legal_moves)

    r, p = self.input_position(l_m = legal_moves)
    
    
    b.p1_make_move(r, p ,team)
    print(f"Team {team} placed a piece at {coordinates_to_notation(r, p)}")
    
    #Evaluates if the newly placed piece creates a mill
    num_mills = b.mills_at(r, p, team)
  
    #Allow user to remove a piece for each mill
    if num_mills > 0 :
      self.use_mills(num_mills=num_mills, team=team, b=b)

    b.print_board()

  
    
  #Function to make a move in phase 2
  def make_p2_move(self, team, b):
  
    #List to store legal moves at a certain position
    legal_pieces = []

    #While loop to find the legal moves for the team (make this into a method for board (61-76)  
    #List with all points a certain team has pieces on
    a_pieces = b.available_pieces(team)
  

    for piece in a_pieces:
      o_r = int(piece[0])
      o_p = int(piece[1])
      p_legal_moves = b.p2_legal_moves_notation(o_r, o_p)
      print(f"Num legal moves for {piece}: {len(p_legal_moves)}")

      # Add to legal pieces array if greater than 0 legal moves
      if len(p_legal_moves) > 0:
        legal_pieces.append(piece)
    
    b.print_board()
    

    
    # Origin Position 
    print("Set Origin Position")
    print("Legal pieces", legal_pieces)
    o_r, o_p = self.input_position(legal_pieces)
    origin = str(o_r) + str(o_p)
    print(f"Legal moves for {origin}: {b.p2_legal_moves_notation(o_r, o_p)}")

    
    #Generating a random move after a valid piece at a position with 0 > legal moves has been selected by the while loop
    a_moves = b.p2_legal_moves_notation(o_r, o_p)
    move_to = ""
    n_r, n_p = self.input_position(a_moves)
    move_to = str(n_r) + str(n_p)
    
  
    #Making the randomized phase 2 move and returning the "coordinates" of the move 
    b.p2_make_move(n_r, n_p, team, o_r, o_p)
    print(f"Moved piece at {origin} to {move_to} for team {team}")
    
    num_mills = b.mills_at(n_r, n_p, team)
    
    #Allow user to remove a piece for each mill
    if num_mills > 0 :
      self.use_mills(num_mills=num_mills, team=team, b=b)
    
    b.print_board()
    return n_r, n_p
