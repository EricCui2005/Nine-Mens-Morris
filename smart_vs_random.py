from game import play_game
import randomAI
import smart_player
import scorers

# Parameters for trial
smith = smart_player.smart_player()
randy = randomAI.randomAI()
scorer = scorers.Scorers()
results = [0, 0, 0]
# Set depth for the Smart Turn here
depth = 1
# Set the scorer function
smart_scorer = scorer.intermediate_board_score

# Set the team names - will be used for trial name
team_names = {0: "Unknown", 2: f"Intermediate Smart Turn with Depth {depth}", 1: "Random", 3: "Stalemate"}

# Set the number of trials
num_trials = 250
trial_name = f"{team_names[1]} vs {team_names[2]}"

def team2_p1_move(team, b, completed_turns):
	smith.MM_move(team, b,
                      depth, completed_turns, smart_scorer)

def team1_p1_move(team, b, completed_turns):
	randy.random_p1_move(team, b)

def team2_p2_move(team, b, completed_turns):
	smith.MM_move(team, b, depth, completed_turns, smart_scorer)

def team1_p2_move(team, b, completed_turns):
	randy.random_p2_move(team, b)
	

print(f"Running Trial: {trial_name}")
for trial in range(num_trials):
	winner, _ = play_game(team1_p1_move, team2_p1_move, team1_p2_move, team2_p2_move)
	print(f"Winner: {team_names[winner]} | Trial {trial + 1}")
	results[winner - 1] += 1

print(f"Results for Trial: {trial_name}")
for i, result in enumerate(results):
	print(f"Number of games for {team_names[i + 1]}: {result}")
