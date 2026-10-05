class Player:
    def __init__(self, name: str):
        self.points = 0
        self.result = ""
        self.name = name

class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.result = ""
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self._lookup = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    @property
    def highest_score(self):
        return self.player1.points if self.player1.points > self.player2.points else self.player2.points        

    @property
    def lowest_score(self):
        return self.player1.points if self.player1.points < self.player2.points else self.player2.points

    @property
    def highest_result_string(self):
        return self.player1.result if self.player1.points > self.player2.points else self.player2.result      

    @highest_result_string.setter
    def highest_result_string(self, new_result):
        if self.player1.points > self.player2.points:
            self.player1.result = new_result
        else:
            self.player2.result = new_result

    @property
    def lowest_result_string(self):
        return self.player1.result if self.player1.points < self.player2.points else self.player2.result      

    @lowest_result_string.setter
    def lowest_result_string(self, new_result):
        if self.player1.points < self.player2.points:
            self.player1.result = new_result
        else:
            self.player2.result = new_result

    @property
    def highest_player_name(self):
        return self.player1.name if self.player1.points > self.player2.points else self.player2.name

    @property
    def lowest_player_name(self):
        return self.player1.name if self.player1.points < self.player2.points else self.player2.name

    def as_tuple(self):
        return (self.result, self.player1.result, self.player2.result)

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score()
        else:
            self.p2_score()

    def tied_score(self):
        if self.player1.points == self.player2.points and self.player1.points < 3:
            self.result = self._lookup.get(self.player1.points, "")
            self.result += "-All"

    def deuce(self):
        if self.player1.points == self.player2.points and self.player1.points > 2:
            self.result = "Deuce"

    def one_player_has_points(self):
        if self.highest_score > 0 and self.lowest_score == 0:
            self.highest_result_string = self._lookup.get(self.highest_score, "")
            self.lowest_result_string = self._lookup[0]
            self.result = self.player1.result + "-" + self.player2.result

    def one_player_has_more_points(self):
        if self.highest_score > self.lowest_score and self.highest_score < 4:
            self.highest_result_string = self._lookup.get(self.highest_score, "")
            self.lowest_result_string = self._lookup.get(self.lowest_score, "")
            self.result = self.player1.result + "-" + self.player2.result

    def one_player_has_advantage(self):
        if self.lowest_score >= 3:
            self.result = f"Advantage {self.highest_player_name}"

    def one_player_wins(self):
        if (
            self.highest_score >= 4
            and self.lowest_score >= 0
            and (self.highest_score- self.lowest_score) >= 2
        ):
            self.result = f"Win for {self.highest_player_name}"

    def score(self):
        self.tied_score()
        if self.result:
            return self.result

        self.deuce()
        if self.result:
            return self.result

        self.one_player_has_points()
        self.one_player_has_more_points()
        self.one_player_has_advantage()
        self.one_player_wins()
        return self.result

    def p1_score(self):
        self.player1.points += 1

    def p2_score(self):
        self.player2.points += 1
