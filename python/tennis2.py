class GameState:
    def __init__(self, player1_name, player2_name):
        self.result = ""
        self.p1res = ""
        self.p2res = ""
        self.p1points = 0
        self.p2points = 0
        self.player1_name = player1_name
        self.player2_name = player2_name

    @property
    def highest_score(self):
        return self.p1points if self.p1points > self.p2points else self.p2points        

    @property
    def lowest_score(self):
        return self.p1points if self.p1points < self.p2points else self.p2points

    @property
    def highest_result_string(self):
        return self.p1res if self.p1points > self.p2points else self.p2res      

    @highest_result_string.setter
    def highest_result_string(self, new_result):
        if self.p1points > self.p2points:
            self.p1res = new_result
        else:
            self.p2res = new_result

    @property
    def lowest_result_string(self):
        return self.p1res if self.p1points < self.p2points else self.p2res      

    @lowest_result_string.setter
    def lowest_result_string(self, new_result):
        if self.p1points < self.p2points:
            self.p1res = new_result
        else:
            self.p2res = new_result


    def as_tuple(self):
        return (self.result, self.p1res, self.p2res)

class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.gamestate = GameState(player1_name, player2_name)
        self._lookup = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score()
        else:
            self.p2_score()

    def tied_score(self):
        if self.gamestate.p1points == self.gamestate.p2points and self.gamestate.p1points < 3:
            self.gamestate.result = self._lookup.get(self.gamestate.p1points, "")
            self.gamestate.result += "-All"

    def deuce(self):
        if self.gamestate.p1points == self.gamestate.p2points and self.gamestate.p1points > 2:
            self.gamestate.result = "Deuce"

    def one_player_has_points(self):
        if self.gamestate.highest_score > 0 and self.gamestate.lowest_score == 0:
            self.gamestate.highest_result_string = self._lookup.get(self.gamestate.highest_score, "")
            self.gamestate.lowest_result_string = self._lookup[0]
            self.gamestate.result = self.gamestate.p1res + "-" + self.gamestate.p2res


    def one_player_has_more_points(self):
        if self.gamestate.highest_score > self.gamestate.lowest_score and self.gamestate.highest_score < 4:
            self.gamestate.highest_result_string = self._lookup.get(self.gamestate.highest_score, "")
            self.gamestate.lowest_result_string = self._lookup.get(self.gamestate.lowest_score, "")
            self.gamestate.result = self.gamestate.p1res + "-" + self.gamestate.p2res

    def p1_has_advantage(self):
        if self.gamestate.p1points > self.gamestate.p2points and self.gamestate.p2points >= 3:
            self.gamestate.result = "Advantage player1"

    def p2_has_advantage(self):
        if self.gamestate.p2points > self.gamestate.p1points and self.gamestate.p1points >= 3:
            self.gamestate.result = "Advantage player2"

    def p1_wins(self):
        if (
            self.gamestate.p1points >= 4
            and self.gamestate.p2points >= 0
            and (self.gamestate.p1points - self.gamestate.p2points) >= 2
        ):
            self.gamestate.result = "Win for player1"

    def p2_wins(self):
        if (
            self.gamestate.p2points >= 4
            and self.gamestate.p1points >= 0
            and (self.gamestate.p2points - self.gamestate.p1points) >= 2
        ):
            self.gamestate.result = "Win for player2"

    def score(self):
        self.tied_score()
        if self.gamestate.result:
            return self.gamestate.result
        self.deuce()
        if self.gamestate.result:
            return self.gamestate.result
        self.one_player_has_points()
        self.one_player_has_more_points()

        self.p1_has_advantage()
        self.p2_has_advantage()
        self.p1_wins()
        self.p2_wins()

        return self.gamestate.result

    def p1_score(self):
        self.gamestate.p1points += 1

    def p2_score(self):
        self.gamestate.p2points += 1
