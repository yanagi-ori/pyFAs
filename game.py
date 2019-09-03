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

    def start_generation(self, amount):
        stories = ["wunderkind", "middle", "slogger", "overhype", "loser", "idler"]
        happyornot = ["happy", "not happy"]
        for i in range(amount):
            new_player = self.create_player(name='new player of ' + self.name, age=random.randint(15, 45),
                               story=stories[random.randint(0, len(stories)-1)], positions="test", team_name=self.name,
                               contract="test", happiness=happyornot[random.randint(0, 1)])
            print(new_player)
            self.players.append(new_player)

    def create_player(self, name, age, story, positions, team_name, contract, happiness):
        """
        имеется в виду то, что игрока воспитывает клубная академия, это дает возможность дальнейшего развития

        backstory:
        wunderkind - игрок, выдающихся способностей
        middle - просто середняк
        slogger - не был одарен природой, но упорством может добиться многого
        overhype - переоцененный
        loser - был одарен, но не карьера не сложилась
        idler - лентяй

        club - кому сейчас принадлежит игрок
        """

        if story == "wunderkind":
            lvl = 30
            mul = (0.1, 0.08, 0.05)
        elif story == "middle":
            lvl = 20
            mul = (0.04, 0.04, 0.01)
        elif story == "slogger":
            lvl = 15
            mul = (0.04, 0.06, 0.03)
        elif story == "overhype":
            lvl = 30
            mul = (0.05, 0.03, 0.0)
        elif story == "loser":
            lvl = 15
            mul = (0.03, 0.02, 0.1)
        elif story == "idler":
            lvl = 25
            mul = (0.03, 0.01, 0.0)
        else:
            print("missed")
            lvl = 0.0
            mul = (0.0, 0.0, 0.0)

        if age <= 20:
            lvl += gen_year(age - 14, 0.1, 0.7, mul[0])
        if 20 < age <= 32:
            lvl += gen_year(age - 14, 0.1, 0.7, mul[0])
            lvl += gen_year(age=12, low=0.0, high=0.06, mul=mul[1])
        if age > 32:
            lvl += gen_year(age - 14, 0.1, 0.7, mul[0])
            lvl += gen_year(age=12, low=0.0, high=0.06, mul=mul[1])
            lvl += gen_year(age=15, low=0.0, high=0.04, mul=mul[1], decrease=True)

        return Player(name=name, age=age, lvl=lvl,
                      positions=positions, team_name=team_name, contract=contract,
                      happiness=happiness, story=story)


class Player:
    def __str__(self):
        return ", ".join([str(self.name), "age: " + str(self.age), "lvl: " + str(self.lvl), str(self.story)])

    def __init__(self, name, age, lvl, positions, team_name, contract, happiness, story):
        self.name = name
        self.age = age
        self.lvl = lvl
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
                new_team.start_generation(temp_data.get('players'))
                league.add_team(new_team)
            this_game_session.add_league(league)


def gen_year(age, low, high, mul, decrease=False):
    dec = 0.0
    period = 0
    if decrease is True:
        if period == 4:
            dec -= 0.01
            period = 0
        period += 1

    for year in range(age):
        return round(random.triangular(low - dec, high - dec, mul - dec) * 100)


game = StartGame()
