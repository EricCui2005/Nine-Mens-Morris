from game import play_game
import randomAI
import scorers

randall = randomAI.randomAI()
randy = randomAI.randomAI()
scorer = scorers.Scorers()
results = [0, 0, 0]
team_names = {1: "Random A", 2: "Random B", 3: "Stalemate"}
num_trials = 1000

def team1_p1_move(team, b, completed_turns):
	randall.random_p1_move(team, b)

def team2_p1_move(team, b, completed_turns):
	randy.random_p1_move(team, b)

def team1_p2_move(team, b, completed_turns):
	randall.random_p2_move(team, b)

def team2_p2_move(team, b, completed_turns):
	randy.random_p2_move(team, b)

for trials in range(num_trials):
	winner = play_game(team1_p1_move, team2_p1_move, team1_p2_move, team2_p2_move, MAX_TURNS=10000)
	print(winner)
	print(f"Winner: {team_names[winner]}")
	results[winner - 1] += 1

for i, result in enumerate(results):
	print(f"Number of games for {team_names[i + 1]}: {result}")