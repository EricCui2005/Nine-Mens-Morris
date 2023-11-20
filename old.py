# # Populate the board with random stuff
# for r in range(3):
#     for p in range(8):
#         b.p1_make_move(r, p, (p % 2 + r % 2) * 5 % 2)

# b.full_board[0][1].occupied = 0
# b.print_board()
# # # Test the Phase 1 Legal Moves Calculator
# # print("Phase 1 Legal Moves")
# b.print_board()
# print()
# print(b.p1_legal_moves())
# print()

# # Test the Phase 2 Legal Moves Calculator
# print("Phase 2 Legal Moves")
# b.print_board()
# print()
# for r in range(3):
#     for p in range(8):
#       print(f"Legal moves for Region {r} and Position {p}")
#       print(b.p2_legal_moves_notation(r, p))

#Populate the board with random stuff
# for r in range(3):
#     for p in range(8):
#         b.p1_make_move(r, p, (p % 2 + r % 2) * 5 % 2)

# b.full_board[0][0].occupied = 2
# b.full_board[0][1].occupied = 2
# b.full_board[0][2].occupied = 2

# b.print_board()
# b.full_board[0][6].occupied = 1
# b.full_board[0][7].occupied = 1

# # Code to pick 18 random unique positions 

# selected_moves = random.sample(valid_moves, k=18)
# print(selected_moves)
# print ("Random Phase 1")
# # Place down pieces at the 18 positions that were selected
# for valid_move in selected_moves:
#   print(f"Team {team}'s move:")
#   # Read in the region and position index from the move string in valid moves   
#   r, p = valid_move

#   # Char/String to int
#   int_r, int_p = int(r), int(p)
#   b.p1_make_move(int_r, int_p, team)
  
#   num_mills = b.mills_at(int_r, int_p, team)
#   b.print_board()
#   print(f"{num_mills} mills")
#   #Prompt if there is a mill
#   if num_mills > 0:
#     print("There is a mill")
#     # b.print_board()
#     print(f"Team {team}'s move:")
#     for i in range(num_mills):
#       tbr_r = int(input("Region of piece to be removed: "))
#       tbr_p = int(input("Position of piece to be removed: "))
#       b.remove_piece(tbr_r, tbr_p, team)
#   team = opposing_team(team)

# b.print_board()   

# # Code to pick 18 random unique positions 

# selected_moves = random.sample(valid_moves, k=18)
# print(selected_moves)
# print ("Random Phase 1")
# # Place down pieces at the 18 positions that were selected
# for valid_move in selected_moves:
#   print(f"Team {team}'s move:")
#   # Read in the region and position index from the move string in valid moves   
#   r, p = valid_move

#   # Char/String to int
#   int_r, int_p = int(r), int(p)
#   b.p1_make_move(int_r, int_p, team)
  
#   num_mills = b.mills_at(int_r, int_p, team)
#   b.print_board()
#   print(f"{num_mills} mills")
#   #Prompt if there is a mill
#   if num_mills > 0:
#     print("There is a mill")
#     # b.print_board()
#     print(f"Team {team}'s move:")
#     for i in range(num_mills):
#       tbr_r = int(input("Region of piece to be removed: "))
#       tbr_p = int(input("Position of piece to be removed: "))
#       b.remove_piece(tbr_r, tbr_p, team)
#   team = opposing_team(team)

# b.print_board()   