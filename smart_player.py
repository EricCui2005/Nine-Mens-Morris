from point import opposing_team, coordinates_to_notation, notation_to_coordinates
import random
import board_tester as bt
import board
import point
import copy
import player


class smart_player(player.Player):

		# Mini Max Move - move in p1 using a minimax tree of depth set by the depth parameter
		def MM_move(self, team, b, depth, completed_turns, scorer):
				# There are 18 turns in phase 1
				phase = 1
				if completed_turns > 17:
						phase = 2
				legal_turns = self.legal_turns(b, team, phase)
				random.shuffle(legal_turns)

				best_score = -1 * float("inf")
				
				
				best_turn = []
				
				for turn in legal_turns:

						self.make_turn(turn, team, b, phase)
						score = self.mini_max(team, b, depth, completed_turns + 1, scorer, True)
						if best_score < score:
								best_score = score
								best_turn = turn

						self.undo_turn(turn, team, b, phase)

				self.make_turn(best_turn, team, b, phase, test=False)



		def mini_max(self, team, b, depth, completed_turns, scorer, maximize):
				phase = 1
				if completed_turns > 17:
						phase = 2

				# If the depth is zero, return the score for this state
				if depth == 0:
						return scorer(team, b, phase)
				else:
						# Get all legal turns for board state
						legal_turns = self.legal_turns(b, team, phase)

						# Find the the best score
						best_score = 0
						if maximize:
								best_score = -1 * float("inf")
						else:
								best_score = float("inf")

						# iterate through each legal turn and calculate minimax
						for turn in legal_turns:
								# Set the turn in the board state
								self.make_turn(turn, team, b, phase)
								score = self.mini_max(opposing_team(team), b, depth - 1,
																			completed_turns + 1, scorer,
																			not maximize)
								# If the score is better than previous ones, set the new best score
								if maximize:
										best_score = max(score, best_score)
								else:
										best_score = min(score, best_score)
								# Reset the board to its initial state
								self.undo_turn(turn, team, b, phase)
						return -1 * best_score
		# Mini Max Move - move in p1 using a minimax tree of depth set by the depth parameter
		def MM_move_ab(self, team, b, depth, completed_turns, scorer):
			# There are 18 turns in phase 1
			phase = 1
			if completed_turns > 17:
					phase = 2
			legal_turns = self.legal_turns(b, team, phase)
			random.shuffle(legal_turns)

			best_score = -1 * float("inf")
			alpha, beta = -1 * float("inf"), 1 * float("inf")
			best_turn = []
			
			for turn in legal_turns:

					self.make_turn(turn, team, b, phase)
					score = self.mini_max_ab(team, b, depth, completed_turns + 1, scorer, True, alpha, beta)
					if best_score < score:
							best_score = score
							best_turn = turn

					self.undo_turn(turn, team, b, phase)

			self.make_turn(best_turn, team, b, phase, test=False)

			# b.print_board()

		def mini_max_ab(self, team, b, depth, completed_turns, scorer, maximize, alpha, beta):
				phase = 1
				if completed_turns > 17:
						phase = 2

				# If the depth is zero, return the score for this state
				if depth == 0:
						return scorer(team, b, phase)
				else:
						# Get all legal turns for board state
						legal_turns = self.legal_turns(b, team, phase)

						# Find the the best score
						best_score = 0
						if maximize:
								best_score = -1 * float("inf")
						else:
								best_score = float("inf")

						# iterate through each legal turn and calculate minimax
						for turn in legal_turns:
								# Set the turn in the board state
								self.make_turn(turn, team, b, phase)
								score = self.mini_max_ab(opposing_team(team), b, depth - 1,
																			completed_turns + 1, scorer,
																			not maximize, alpha, beta)
							# Reset the board to its initial state
								self.undo_turn(turn, team, b, phase)	
							# If the score is better than previous ones, set the new best score
								if maximize:
										best_score = max(score, best_score)
										if best_score >= beta:
											return -1 * best_score 
										alpha = max(alpha, best_score)
								else:
										best_score = min(score, best_score)
										if best_score <= alpha:
											return -1 * best_score
										beta = min(beta, best_score)
								
						return -1 * best_score