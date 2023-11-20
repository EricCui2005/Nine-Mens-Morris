from game import play_game
import randomAI
import human_player
import scorers

harold = human_player.human_player()
randy = randomAI.randomAI()
scorer = scorers.Scorers()
results = [0, 0, 0]
team_names = {1: "Human", 2: "Random", 3: "Stalemate"}
num_trials = 1000

def team1_p1_move(team, b, completed_turns):
	harold.make_p1_move(team, b)

def team2_p1_move(team, b, completed_turns):
	randy.random_p1_move(team, b)

def team1_p2_move(team, b, completed_turns):
	harold.make_p2_move(team, b)

def team2_p2_move(team, b, completed_turns):
	randy.random_p2_move(team, b)

for trials in range(num_trials):
	winner = play_game(team1_p1_move, team2_p1_move, team1_p2_move, team2_p2_move)
	print(f"Winner: {team_names[winner]}")
	results[winner - 1] += 1

for result in results:
	print(f"Number of games for {team_names[result]}: {result}")