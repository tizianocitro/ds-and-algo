# !difficulty: easy

# There's an algorithms tournament taking place in which teams of programmers compete against each other to solve algorithmic problems as fast as possible.
# Teams compete in a round robin, where each team faces off against all other teams.
# Only two teams compete against each other at a time, and for each competition, one team is designated the home team, while the other team is the away team.
# In each competition there's always one winner and one loser; there are no ties.
# A team receives 3 points if it wins and 0 points if it loses.
# The winner of the tournament is the team that receives the most amount of points.

# Given an array of pairs representing the teams that have competed against each other
# and an array containing the results of each competition, write a function that returns the winner of the tournament.
# The input arrays are named competitions and results, respectively.
# The competitions array has elements in the form of [homeTeam, awayTeam],
# where each team is a string of at most 30 characters representing the name of the team.
# The results array contains information about the winner of each corresponding competition in the competitions array.
# Specifically, results[i] denotes the winner of competitions[i],
# where a 1 in the results array means that the home team in the corresponding competition won and a 0 means that the away team won.

# It's guaranteed that exactly one team will win the tournament and that each team will compete against all other teams exactly once.
# It's also guaranteed that the tournament will always have at least two teams.

# Input:
# competitions = [
#    ["HTML", "C#"],
#    ["C#", "Python"],
#    ["Python", "HTML"],
# ]
# results = [0, 0, 1]
# Output:
# "Python"
# C# beats HIML, Python beats C#, and Python beats HTML
# HTML -> 0 points, C# -> 3 points, Python -> 6 points

# Complexity
# O(n) time - where n is the number of competitions
# O(k) space - where k is the number of key in the dict, which depends on the number of teams

# solution one with the winner setting within the loop to calculate the scores
def tournament_winner(competitions, results):
    scores = dict()
    winner = {"team": "", "score": 0}
    for i, competition in enumerate(competitions):
        home_team, away_team = competition
        if results[i] == 1:
            update_scores(scores, winner, home_team)
        else:
            update_scores(scores, winner, away_team)
    return winner["team"]

def update_scores(scores, winner, team):
    score = scores.get(team, 0) + 1
    scores[team] = score
    update_winner(winner, team, score)

def update_winner(winner, team, score):
    if score > winner["score"]:
        winner["team"] = team
        winner["score"] = score
        
# solution two
def tournament_winner(competitions, results):
    wins = dict()
    winner = {"team": "", "score": 0}
    for i in range(len(competitions)):
        competition = competitions[i]
        home_team = competition[0]
        away_team = competition[1]
        if results[i] == 1:
            score = wins.get(home_team, 0) + 1
            wins[home_team] = score
            update_winner(winner, home_team, score)
        else:
            score = wins.get(away_team, 0) + 1
            wins[away_team] = score
            update_winner(winner, away_team, score)
    return winner["team"]

def updateWinner(winner, team, score):
    if score > winner["score"]:
        winner["team"] = team
        winner["score"] = score