import board
from point import opposing_team 
import randomAI
import greedy
from board_tester import *

#Play will begin with white (team = 1)
team = 2

#Play will begin at phase 1 (freely placing pieces until each team has placed 9 pieces)
phase = 1

#Initializing board object and randomAI to be utilized
b = board.Board()


randy = randomAI.randomAI()
grant = greedy.Greedy()

#Initializing and printing an empty board
print("Initial State")

b = quick_populate(b, ["o1", "o2", "m1", "m3", "m7"], ["i0", "i7", "i4", "i5"])


b.print_board()

#Returns a list of legal moves for phase 1 (simply unoccupied squares)
valid_moves = b.p1_legal_moves()

# Phase 1 Loop that executes until a phase change is detected
while not b.phase_change():

  
  #Code chunk that allows the randomAI to play. Randy plays as white (team = 1)
  if team % 2 == 1:
    randy.random_p1_move(team, b)
		
  #Chunk of code that calls a random move from the randomAI. randomAI plays as black (team = 2)
  else:
    print("Legal moves:", b.p1_legal_moves())
    grant.greedy_p1_move(b, team)

  #Switches play to the opposing team
  team = opposing_team(team)

print("Phase 2 not implemented")

# Phase 2 While Loop 


#Phase 2 terminates and the corresponding team wins when the opposing team has 2 or less pieces on the board or the opposing team has no more legal moves
while not b.is_win_for_team(team):

  #Code chunk allows the human player to make a move in phase 2. The human is still playing as white (team = 1)
  if team % 2 == 1:
    randy.random_p2_move(team, b)
  else:
    randy.random_p2_move(team, b)
  #Checking if the most recent move caused a win condition
  if b.is_win_for_team(team):
    break
  team = opposing_team(team)
  b.print_board()

print(f"Team {team} wins")


    
  

