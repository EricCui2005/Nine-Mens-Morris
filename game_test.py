from game import play_game
import randomAI
import smart_player
import scorers

smith = smart_player.smart_player()
randy = randomAI.randomAI()
scorer = scorers.Scorers()
wins = [0, 0]
team_names = {1: "Greedy", 2: "Random"}





def team1_p1_move(team, b, completed_turns):
	smith.MM_move(team, b, 2, completed_turns, scorer.intermediate_board_score)

def team2_p1_move(team, b, completed_turns):
	randy.random_p1_move(team, b)

def team1_p2_move(team, b, completed_turns):
	smith.MM_move(team, b, 2, completed_turns, scorer.intermediate_board_score)

def team2_p2_move(team, b, completed_turns):
	randy.random_p2_move(team, b)

winner = play_game(team1_p1_move, team2_p1_move, team1_p2_move, team2_p2_move)
print(f"Winner: f{team_names[winner]}")

  