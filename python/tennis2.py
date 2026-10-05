class GameState:
    def __init__(self):
        self.result = ""
        self.p1res = ""
        self.p2res = ""
        self.p1points = 0
        self.p2points = 0

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
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.gamestate = GameState()

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score()
        else:
            self.p2_score()

    def tied_score(self):
        if self.gamestate.p1points == self.gamestate.p2points and self.gamestate.p1points < 3:
            if self.gamestate.p1points == 0:
                self.gamestate.result = "Love"
            if self.gamestate.p1points == 1:
                self.gamestate.result = "Fifteen"
            if self.gamestate.p1points == 2:
                self.gamestate.result = "Thirty"
            self.gamestate.result += "-All"

    def deuce(self):
        if self.gamestate.p1points == self.gamestate.p2points and self.gamestate.p1points > 2:
            self.gamestate.result = "Deuce"

    def one_player_has_points(self):
        if self.gamestate.highest_score > 0 and self.gamestate.lowest_score == 0:
            if self.gamestate.highest_score == 1:
                self.gamestate.highest_result_string = "Fifteen"
            if self.gamestate.highest_score == 2:
                self.gamestate.highest_result_string = "Thirty"
            if self.gamestate.highest_score == 3:
                self.gamestate.highest_result_string = "Forty"

            self.gamestate.lowest_result_string = "Love"
            self.gamestate.result = self.gamestate.p1res + "-" + self.gamestate.p2res


    def one_player_has_more_points(self):
        if self.gamestate.highest_score > self.gamestate.lowest_score and self.gamestate.highest_score < 4:
            if self.gamestate.highest_score == 2:
                self.gamestate.highest_result_string = "Thirty"
            if self.gamestate.highest_score == 3:
                self.gamestate.highest_result_string = "Forty"
            if self.gamestate.lowest_score == 1:
                self.gamestate.lowest_result_string = "Fifteen"
            if self.gamestate.lowest_score == 2:
                self.gamestate.lowest_result_string = "Thirty"
            self.gamestate.result = self.gamestate.p1res + "-" + self.gamestate.p2res

    def score(self):
        self.tied_score()
        if self.gamestate.result:
            return self.gamestate.result
        self.deuce()
        if self.gamestate.result:
            return self.gamestate.result
        self.one_player_has_points()
        self.one_player_has_more_points()


        if self.gamestate.p1points > self.gamestate.p2points and self.gamestate.p2points >= 3:
            self.gamestate.result = "Advantage player1"

        if self.gamestate.p2points > self.gamestate.p1points and self.gamestate.p1points >= 3:
            self.gamestate.result = "Advantage player2"

        if (
            self.gamestate.p1points >= 4
            and self.gamestate.p2points >= 0
            and (self.gamestate.p1points - self.gamestate.p2points) >= 2
        ):
            self.gamestate.result = "Win for player1"
        if (
            self.gamestate.p2points >= 4
            and self.gamestate.p1points >= 0
            and (self.gamestate.p2points - self.gamestate.p1points) >= 2
        ):
            self.gamestate.result = "Win for player2"
        return self.gamestate.result

    def p1_score(self):
        self.gamestate.p1points += 1

    def p2_score(self):
        self.gamestate.p2points += 1
