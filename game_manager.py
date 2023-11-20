import board
import point

class Game_Manager:
  def __init__(self):
    self.team=1
    self.phase=1
    self.won=0

  def get_input(message):
    return input(message)

  def play_game(self):

    b = board.Board()
    while not b.phase_change():
      #if team 1 turn
      if self.team == 1:
        
        #get input
        r = get_input("Enter region: ")
        p = get_input("Enter position: ")
        #place piece
        b.p1_make_move(r, p, self.team)
        #check for mill and remove piece
        if b.mills_at(r, p, self.team) > 0:
          removed_r = get_input("Enter region of removed piece: ")
          removed_p = get_input("Enter position of removed piece: ")
          b.remove_piece(removed_r, removed_p, self.team)
        
        # switch team
        self.team = self.team + 1 % 2

    #if team 2 turn
    else:
        #get input
        #place piece
        #check for mill and remove piece
        # check for win
        # if won, set won to player team
        # switch team
      

  

  