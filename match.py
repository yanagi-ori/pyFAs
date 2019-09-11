import random


class Match:
    def __init__(self, team1, team2):
        self.score = [0, 0]
        self.team1 = team1
        self.team2 = team2
        self.teams = [team1, team2]

    def simulation(self):
        team1_full = sum(self.team1.strength)
        team2_full = sum(self.team2.strength)

        num_of_rounds = (team1_full - team2_full) // 10
        if num_of_rounds < 0:
            if random.randint(0, 100) > 50: self.score[1] += 1
            for i in range(num_of_rounds):
                if self.score[0] == 10 or self.score[1] == 10: break  # ограничение числа голов.
                # не очень правильно, возможно, потом переделаю
                temp = self.round_simulation(self.team2, self.team1)
                if temp == self.team1:
                    self.score[0] += 1
                else:
                    self.score[1] += 1
        elif num_of_rounds > 0:
            if random.randint(0, 100) > 50: self.score[0] += 1
            for i in range(num_of_rounds):
                temp = self.round_simulation(self.team1, self.team2)
                if temp == self.team1:
                    self.score[0] += 1
                elif temp == self.team2:
                    self.score[1] += 1

        if random.randint(0, 100) > 50: self.score[0] += 1
        if random.randint(0, 100) > 50: self.score[1] += 1
        return self.score

    def round_simulation(self, attackers, defenders):
        attackers_in_def = attackers.strength[1] + attackers.strength[2] // 2
        attackers_in_atk = attackers.strength[2] + attackers.strength[3]
        defenders_in_def = defenders.strength[1] + defenders.strength[2] // 2
        defenders_in_atk = defenders.strength[2] + defenders.strength[3]
        if attackers_in_atk + random.randint(0, 25) > defenders_in_def + random.randint(0, 20):
            if attackers.line_up[3][random.randint(0, 1)].lvl \
                    + random.randint(0, 10) > defenders.line_up[0][0].lvl + random.randint(30, 60):
                return attackers
        elif defenders_in_atk + random.randint(50, 100) > attackers_in_def:
            if defenders.line_up[3][random.randint(0, 1)].lvl + random.randint(0, 60) > attackers.line_up[0][0].lvl:
                return defenders
