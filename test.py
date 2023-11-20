import board
from point import opposing_team 
import random
import randomAI
import math
import smart_player
from board_tester import *

#Play will begin with white (team = 1)
team = 2

#Play will begin at phase 1 (freely placing pieces until each team has placed 9 pieces)
phase = 1

#Initializing board object and randomAI to be utilized
b = board.Board()

smith = smart_player.smart_player()
randy = randomAI.randomAI()

b = quick_populate(b, ["o1", "o2", "m1", "m3", "m7"], ["i0", "i7", "i4", "i5", "o5"])

legal_turns = smith.legal_turns(b, team, phase)

def get_notation(turn):
	o, m, r = turn
	if o is not None:
		o = o.notation
	if m is not None:
		m = m.notation
	if r is not None:
		r = r.notation
	return o, m, r


notations = [get_notation(p) for p in legal_turns]

best_score, best_turn = -1, []

b.print_board() 
for turn in legal_turns:
	smith.make_p1_turn(turn, team, b)
	score = smith.complex_board_score(team, b)
	if score > best_score:
		best_score = score
		best_turn = turn
	smith.undo_p1_turn(turn, team, b)

print(f" Best Turn: {get_notation(turn)}")
smith.make_p1_turn(turn, team, b)
b.print_board()
# print(legal_moves)

# print(smith.complex_board_score(1, b))
# print(smith.complex_board_score(2, b))

