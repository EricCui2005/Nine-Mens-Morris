from game import play_game
import smart_player
import scorers

# Parameters for trial
smith = smart_player.smart_player()
steven = smart_player.smart_player()
scorer = scorers.Scorers()
results = [0, 0, 0]
depth_1, depth_2 = 2, 2
scorer_1, scorer_2 = scorer.intermediate_board_score, scorer.simple_board_score
team_names = {0: "Unknown", 1: f"Intermediate Smart Turn with Depth {depth_1}", 2: f"Simple Smart Turn with Depth {depth_2}", 3: "Stalemate"}
num_trials = 100
trial_name = f"{team_names[1]} vs {team_names[2]}"

def team1_p1_move(team, b, completed_turns):
	smith.MM_move(team, b, depth_1, completed_turns, scorer_1)

def team2_p1_move(team, b, completed_turns):
	steven.MM_move(team, b, depth_2, completed_turns, scorer_2)


def team1_p2_move(team, b, completed_turns):
	smith.MM_move(team, b, depth_1, completed_turns, scorer_1)

def team2_p2_move(team, b, completed_turns):
	steven.MM_move(team, b, depth_2, completed_turns, scorer_2)

print(f"Running Trial: {trial_name}")
for trial in range(num_trials):
	winner, _ = play_game(team1_p1_move, team2_p1_move, team1_p2_move, team2_p2_move)
	print(f"Winner: {team_names[winner]} | Trial {trial + 1}")
	results[winner - 1] += 1

print(f"Results for Trial: {trial_name}")
for i, result in enumerate(results):
	print(f"Number of games for {team_names[i + 1]}: {result}")
