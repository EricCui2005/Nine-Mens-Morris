from point import Point, same_team, opposing_team

class Invalid_Move(Exception):
    pass
# Declaring the overarching board class
class Board:

    # Declaring the point class to store information about each point the players have to operate with

    def __init__(self):

        # # The number of each team's pieces on the board at the present moment
        self._num_white_on_board = 0
        self._num_black_on_board = 0

        # The number of each pieces each team has placed to date (used to determine when to switch to phase 2)
        self._num_white_placed = 0
        self._num_black_placed = 0

        # Initializing the Board with Points
        full_board = [[], [], []]
        point_names = {"outer": "o", "middle": "m", "inner": "i"}

        for region_i, region in enumerate(["outer", "middle", "inner"]):
            for position in range(8):
                # notation = point_names[region] + str(position)
                notation = str(region_i) + str(position)
                full_board[region_i].append(
                    Point(0, notation, region_i, position))
        self.full_board = full_board

    @property
    def num_white_on_board(self):
        return self._num_white_on_board
    
    @property
    def num_black_on_board(self):
        return self._num_black_on_board
      
    @property
    def num_white_placed(self):
        return self._num_white_placed
    
    @property
    def num_black_placed(self):
        return self._num_black_placed
      
    # Function to print the board
    def print_board(self):

        # Printing layer 1
        for i in range(3):
            print(self.full_board[0][i], end="")
            if i == 2:
                break
            print("----", end="")
        print()

        # Printing layer 2

        print("|", end="")
        print(" ", end="")
        for i in range(3):
            print(self.full_board[1][i], end="")
            if i == 2:
                break
            print("--", end="")

        print(" |", end="")

        print()

        # Printing layer 3
        print("|", end="")
        print(" | ", end="")
        for i in range(3):
            print(self.full_board[2][i], end="")
        print(" | |", end="")

        print()

        # Printing layer 4
        print(self.full_board[0][7], end="")
        print("-", end="")
        print(self.full_board[1][7], end="")
        print("-", end="")
        print(self.full_board[2][7], end="")

        print(" ", end="")

      
        
        print(self.full_board[2][3], end="")
        print("-", end="")
        print(self.full_board[1][3], end="")
        print("-", end = "")
        print(self.full_board[0][3], end="")
        
        print()

        # Printing layer 5
        print("|", end="")

        print(" | ", end="")

        for i in range(3):
            print(self.full_board[2][6 - i], end="")
        print(" | ", end="")

        print("|", end="")

        print()

        # Printing layer 6
        print("| ", end="")
        for i in range(3):
            print(self.full_board[1][6 - i], end="")
            if i == 2:
                break
            print("--", end="")
        print(" |", end="")

        print()

        # Printing layer 7
        for i in range(3):
            print(self.full_board[0][6 - i], end="")
            if i == 2:
                break
            print("----", end="")
        print()


#phase 1
# Evaluate if a move is legal in phase 1

    def legal_move(self, region, position):
        return self.full_board[region][position].occupied == 0

    # Give a list of legal moves for a player during phase 1
    def p1_legal_moves(self):

        legal_moves = []
        #Iterate through regions
        for r in range(3):
            for p in range(8):
                if not self.full_board[r][p].occupied:
                    legal_moves.append(self.full_board[r][p].notation)
        return legal_moves

    # Function to make a move in phase 1 (the pieces can be freely placed into any open area on the board)
    def p1_make_move(self, region, position, team):
        # Evaluating if the selected move is legal or not
        if self.legal_move(region, position):
            # Team => 1 = white, 2 = black
            self.full_board[region][position].occupied = team
            # Tracking the number of pieces placed for each team as well as the number of pieces each team has on the board for phase and game tracking purposes
            if team == 1:
                self._num_white_placed += 1
                self._num_white_on_board += 1
            if team == 2:
                self._num_black_placed += 1
                self._num_black_on_board += 1
        # Exception to inform the user the move is illegal (space is occupied)
        else:
            print("Space is Occupied")
            raise Invalid_Move

    # Checks whether or not to change the phase of the game based on if each team has exhausted the number of phase 1 pieces they can place
    def phase_change(self):
        return self.num_white_placed == 9 and self.num_black_placed == 9

    #phase 2 legal moves, takes in the "coordinates" of a certain testing position to return a list of legal moves from that testing position
    def p2_legal_moves_notation(self, region, position):
        # List to store legal moves (stored as notation)
        moves = []

        # First round of testing position evaluation. Each piece in phase 2 has the possibility of moving either "forward" or "backward" within their own square. Pieces in even numbered positions can only move in this manner, while pieces in odd numbered positions have the additional possibility of moving from square to square. This first segment of testing position evaluation evaluates whether the points in front of and behind the testing position are legal.

        # Temporary variable to store the information for the legal moves from a certain position being evaluated
        p = self.full_board[region][position]

        # Stores information for the position ahead of the even-numbered testing position
        pf = self.full_board[region][(p.position + 1) % 8]

        # Stores information for the position behind the even-numbered testing position
        pb = self.full_board[region][(p.position - 1) % 8]

        # Adding the notation of the afforementioned testing positions to the list of legal moves if they are unoccupied
        if pb.occupied == 0:
            moves.append(pb.notation)

        if pf.occupied == 0:
            moves.append(pf.notation)

        # Second round of additional evaluation for odd-numbered positions. This segment of code is evaluating whether moving from the testing position to another available square is legal. Available squares depend based on the point
        if position % 2 == 1:

            #moving up a region (allowed for region 0 and 1)
            if region == 0 or region == 1:
                if self.full_board[region + 1][position].occupied == 0:
                    moves.append(self.full_board[region +
                                                 1][position].notation)

            #moving back a region (allowed for region 1 and 2)
            if region == 1 or region == 2:
                if self.full_board[region - 1][position].occupied == 0:
                    moves.append(self.full_board[region -
                                                 1][position].notation)
        return moves

    #make move
    def p2_make_move(self, region, position, team, origin_region,
                     origin_position):

        #Make sure that the move is legal
        if self.full_board[region][position].occupied:
            raise "Not a legal move"

        if not self.full_board[origin_region][origin_position].occupied:
            raise "Not a legal move"

        if not self.full_board[region][position].notation in self.p2_legal_moves_notation(
                origin_region, origin_position):
            raise "Not a legal move"

        self.full_board[origin_region][origin_position].occupied = 0
        self.full_board[region][position].occupied = team

    #is in mill. This function will evaluate whether or not a certain occupied position is part of a mill (three occupied positions in a row). It will return 0 for no mills, 1 for being part of one mill, and 2 if the position is a part of 2 mills
    def mills_at(self, region, position, team):

        #Temporary variable to store the information for the position being evaluated
        p = self.full_board[region][position]
      
        #P is not the same team
        if p.occupied != team:
            #Should not happen
            return 0
  
        #Points located "+1" and "+2" (clockwise) of the testing position
        pf_1 = self.full_board[region][(p.position + 1) % 8]
        pf_2 = self.full_board[region][(p.position + 2) % 8]

        #Points located "-1" and "-2" (counterclockwise) of the testing position
        pb_1 = self.full_board[region][(p.position - 1) % 8]
        pb_2 = self.full_board[region][(p.position - 2) % 8]

        total = 0
        #Even Case (0 = not in a mill, 1 = in one mill, 2 = in two mills)
        if position % 2 == 0:
            # Mill going forward
            if same_team(p, pf_1) and same_team(p, pf_2):
                total += 1
            # Mill going backward
            if same_team(p, pb_1) and same_team(p, pb_2):
                total += 1

            return total

        else:
            # Mill going horizontally
            if same_team(p, pf_1) and same_team(p, pb_1):
                total += 1
            # Mill going vertically
            p0 = self.full_board[0][p.position]
            p1 = self.full_board[1][p.position]
            p2 = self.full_board[2][p.position]
            if same_team(p0, p1) and same_team(p1, p2):
                total += 1
            return total


    def remove_piece(self, region, position, removing_team):
        #Check if piece is opposite team and occupied
        if self.full_board[region][position].occupied != removing_team and self.full_board[
                region][position].occupied != 0:
            # remove piece
            self.full_board[region][position].occupied = 0
    
        else:
            raise "Choose another Piece"
    
    def is_win_for_team(self, team):
    
      num_opp_pieces = 0
      #Check if there are no more legal moves and find the number of opposing pieces
      opponent = opposing_team(team)
      
      possible_moves = []
      for r in range(3):
          for p in range(8):
            #Check the pieces 
            if self.full_board[r][p].occupied == opponent:
              num_opp_pieces += 1
              possible_moves.extend(self.p2_legal_moves_notation(r, p))
      return len(possible_moves) <= 0 or num_opp_pieces <= 2

    #Function that returns a list of points (in notation form) a certain team (passed in as a parameter) has pieces on
    def available_pieces(self, team):
      #Empty list to store every point the team to be evaluated has pieces on
      team_pieces = []
      
      for i in range(3):
        for j in range(8):
          if self.full_board[i][j].occupied == team:
            team_pieces.append(self.full_board[i][j].notation)

      return team_pieces
          