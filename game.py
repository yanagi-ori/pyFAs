import json
import random


class League:
    def __init__(self, name):
        self.name = name
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def show(self):
        for team in self.teams:
            print(team)


class Team:
    def __init__(self, name, lvl, budget):
        self.name = name
        self.lvl = lvl
        self.budget = budget
        self.players = []
'''
    def create_player(self, age, story, club):
        """
        имеется в виду то, что игрока воспитывает клубная академия, это дает возможность дальнейшего развития

        age:
        young (15-20)
        middle (21-29)
        veteran (30-45)

        backstory:
        wunderkind - игрок, выдающихся способностей
        middle - просто середняк
        slogger - не был одарен природой, но упорством может добиться многого
        overhype - переоцененный
        loser - был одарен, но не карьера не сложилась
        idler - лентяй

        club - кому сейчас принадлежит игрок
        """

        if story == "wunderkind": mul = 0.04, 
        if story == "middle" : mul = 0.03
        if story == "slogger": mul = 0.02
        if story == "overhype" : mul = 0.04
        if story == "loser": 

        name = 'test player'
        lvl = 10
        age -= 14
        if age <= 20:
            for year in range(age):
                lvl += random.triangular(0.0, 0.05, mul)'''


class Player:
    def __init__(self, name, age, positions, team_name, contract, happiness, story):
        self.name = name
        self.age = age
        self.positions = positions
        self.team_name = team_name
        self.contract = contract
        self.happiness = happiness
        self.story = story


class Contract:
    def __init__(self, salary, duration, role):
        self.salary = salary
        self.duration = duration
        self.role = role


class Game:
    def __init__(self):
        self.root_of_leagues = []

    def add_league(self, league):
        self.root_of_leagues.append(league)


class StartGame:
    def __init__(self):
        this_game_session = Game()
        with open("package.json", "r") as read_file:
            data = json.load(read_file)
        print(data)
        leagues_list = data.get("leagues")
        teams_list = data.get("teams")
        print(leagues_list)
        for league_name in leagues_list.keys():
            teams_in_league = leagues_list.get(league_name)
            league = League(league_name)
            print(teams_in_league)
            for team in teams_in_league:
                temp_data = teams_list.get(team)
                new_team = Team(name=team, lvl=temp_data.get('lvl'), budget=temp_data.get('budget'))
                league.add_team(new_team)
            league.show()
            this_game_session.add_league(league)


game = StartGame()
