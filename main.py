from game import play_game
import human_player
import scorers

harold = human_player.human_player()
henry = human_player.human_player()
scorer = scorers.Scorers()
results = [0, 0, 0]
team_names = {1: "Human A", 2: "Human B", 3: "Stalemate"}

def team1_p1_move(team, b, completed_turns):
	harold.make_p1_move(team, b)

def team2_p1_move(team, b, completed_turns):
	henry.make_p1_move(team, b) 

def team1_p2_move(team, b, completed_turns):
	harold.make_p2_move(team, b)

def team2_p2_move(team, b, completed_turns):
	henry.make_p2_move(team, b)


winner = play_game(team1_p1_move, team2_p1_move, team1_p2_move, team2_p2_move)
print(f"Winner: {team_names[winner]}")