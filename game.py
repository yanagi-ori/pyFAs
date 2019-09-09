import copy
import json
import random

import render


class League:
    def __init__(self, name):
        self.name = name
        self.teams = []
        self.calendar = []
        self.week = 0

    def add_team(self, team):
        """ adds a new team to the current league """
        self.teams.append(team)

    def create_table(self):
        if len(self.teams) % 2 != 0:  # if there're odd num of teams
            self.teams += [""]  # we add an empty one
            # if some team have a match with it, this team skips this tour
        random.shuffle(self.teams)
        # dividing teams on the two groups
        first_basket = self.teams[:len(self.teams) // 2]
        second_basket = self.teams[len(self.teams) // 2:]
        second_basket.reverse()
        self.calendar.append(self.__generate_pairs__(first_basket, second_basket))
        # during all the tours we create the pairs of teams, the first team in the pair is a home one
        for _ in range(len(self.teams) - 1):
            first_basket, second_basket = self.__round_robin__(first_basket, second_basket)
            self.calendar.append(self.__generate_pairs__(first_basket, second_basket))
        temp = copy.deepcopy(self.calendar)
        temp.reverse()
        self.calendar += temp

    def __generate_pairs__(self, first_part, second_part):
        """ creating pairs of teams - matches """
        week = []
        for i in range(len(first_part)):
            week.append((first_part[i], second_part[i]))
        return week

    def __round_robin__(self, first_part, second_part):
        """
        round-robin algorithm
        The first team in the first array is static,
        The first team from the second array moves to the first array[1], moving other elements to the left,
        The last of the first array moves to the last element of second array, moving other element to the right.
        """
        save = first_part[len(first_part) - 1]
        for i in range(len(first_part) - 1):
            first_part[len(first_part) - 1 - i] = first_part[len(first_part) - 2 - i]
        first_part[1] = second_part[0]
        for i in range(len(second_part) - 1):
            second_part[i] = second_part[i + 1]
        second_part[-1] = save
        return first_part, second_part


class Team:
    def __init__(self, name, lvl, budget):
        self.formation = (1, 4, 4, 2)
        self.name = name
        self.lvl = lvl
        self.budget = budget
        self.players = []
        self.line_up = []  # GK - DF - MD - FW - sub
        self.strength = []  # the same

    def start_generation(self, amount):
        stories = ["wunderkind", "middle", "slogger", "overhype", "loser", "idler"]
        happyornot = ["happy", "not happy"]
        positions = ["GK", "DF", "MD", "FW"]

        for i, amt in enumerate(self.formation):
            for _ in range(amt):
                self.players.append(self.create_player(age=random.randint(15, 45),
                                                       story=stories[random.randint(0, len(stories) - 1)],
                                                       positions=positions[i],
                                                       team_name=self.name,
                                                       contract="empty_field",
                                                       happiness=happyornot[random.randint(0, 1)]))
        if amount - sum(self.formation) > 0:
            for _ in range(amount - sum(self.formation)):
                self.players.append(self.create_player(age=random.randint(15, 45),
                                                       story=stories[random.randint(0, len(stories) - 1)],
                                                       positions=positions[random.randint(0, len(positions) - 1)],
                                                       team_name=self.name,
                                                       contract="empty_field",
                                                       happiness=happyornot[random.randint(0, 1)]))

    def create_player(self, age, story, positions, team_name, contract, happiness):
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
        name = "{0} {1}".format(names_list[random.randint(0, len(names_list)) - 1], surnames_list[
            random.randint(0, len(surnames_list)) - 1])

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

    def add_new_player(self, player):
        self.players.append(player)

    def del_gone_player(self, player):
        self.players.remove(player)

    def sort_on_positions(self):
        pos_list = ["GK", "DF", "MD", "FW"]
        for i in range(4):
            temp = []
            for player in self.players:
                if player.positions == pos_list[i]:
                    temp.append(player)
                    for j in range(len(temp) - 1, 0, -1):  # Sorting players on their position
                        if temp[j].lvl > temp[j - 1].lvl:
                            temp[j], temp[j - 1] = temp[j - 1], temp[j]
            sum_lvl = 0
            for p in temp[:self.formation[i]]:
                sum_lvl += p.lvl
            self.strength.append(sum_lvl)
            self.line_up.append(temp)


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

    def transfer(self, old_team, new_team):
        old_team.del_gone_player(self)
        new_team.add_new_player(self)


class Contract:
    def __init__(self, salary, duration, role):
        self.salary = salary
        self.duration = duration
        self.role = role


class Game:
    def __init__(self, renderer):
        self.renderer = renderer
        self.current_task = "Starting..."
        self.percentage = 0
        self.renderer.render_loading_screen(self.percentage, self.current_task)
        self.root_of_leagues = []
        render.print_at(6, 0, '#' + "Loading Default Data...".center(renderer.width - 2) + '#')
        self.current_task = "Loading Default Data..."
        with open("data/package.json", "r") as read_file:
            data = json.load(read_file)
        leagues_list = data.get("leagues")
        teams_list = data.get("teams")
        self.current_task = "Building Leagues..."
        render.print_at(6, 0, '#' + self.current_task.center(renderer.width - 2) + '#')
        for league_name in leagues_list.keys():
            teams_in_league = leagues_list.get(league_name)
            league = League(league_name)
            for team in teams_in_league:
                self.current_task = "Managing clubs"
                render.print_at(6, 0, '#' + self.current_task.center(renderer.width - 2) + '#')
                temp_data = teams_list.get(team)
                new_team = Team(name=team, lvl=temp_data.get('lvl'), budget=temp_data.get('budget'))
                self.current_task = "Generating new players for {0}...".format(team)
                render.print_at(6, 0, '#' + self.current_task.center(renderer.width - 2) + '#')
                new_team.start_generation(temp_data.get('players'))
                self.current_task = "Adding new team to the league..."
                render.print_at(6, 0, '#' + self.current_task.center(renderer.width - 2) + '#')
                league.add_team(new_team)
            league.create_table()
            self.add_league(league)
        self.percentage = 100
        render.print_at(8, 0, '#' + (str(self.percentage) + '%').center(renderer.width - 2) + '#')

    def add_league(self, league):
        self.root_of_leagues.append(league)


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


names_list = []
surnames_list = []
with open("data/names.txt") as names_file:
    for line in names_file:
        names_list.append(line.strip())
with open("data/surnames.txt") as surnames_file:
    for line in surnames_file:
        surnames_list.append(line.strip())
# game = Game()
current_task = "Starting..."
