from collections import namedtuple


class GameState:
    def __init__(self):
        self.result = ""
        self.p1res = ""
        self.p2res = ""

class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0
        self.gamestate = GameState()

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score()
        else:
            self.p2_score()

    def tied_score(self):
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                self.gamestate.result = "Love"
            if self.p1points == 1:
                self.gamestate.result = "Fifteen"
            if self.p1points == 2:
                self.gamestate.result = "Thirty"
            self.gamestate.result += "-All"

    def deuce(self):
        result = ""
        if self.p1points == self.p2points and self.p1points > 2:
            result = "Deuce"
        return (result, "", "")

    def p1_has_points(self):
        p1res = ""
        p2res = ""
        result = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                p1res = "Fifteen"
            if self.p1points == 2:
                p1res = "Thirty"
            if self.p1points == 3:
                p1res = "Forty"

            p2res = "Love"
            result = p1res + "-" + p2res
        return (result, p1res, p2res)

    def p2_has_points(self, gamestate):
        result, p1res, p2res = gamestate
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                p2res = "Fifteen"
            if self.p2points == 2:
                p2res = "Thirty"
            if self.p2points == 3:
                p2res = "Forty"

            p1res = "Love"
            result = p1res + "-" + p2res
        return (result, p1res, p2res)

    def p1_has_more_points(self, gamestate):
        result, p1res, p2res = gamestate
        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                p1res = "Thirty"
            if self.p1points == 3:
                p1res = "Forty"
            if self.p2points == 1:
                p2res = "Fifteen"
            if self.p2points == 2:
                p2res = "Thirty"
            result = p1res + "-" + p2res
        return (result, p1res, p2res)


    def p2_has_more_points(self, gamestate):
        result, p1res, p2res = gamestate
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                p2res = "Thirty"
            if self.p2points == 3:
                p2res = "Forty"
            if self.p1points == 1:
                p1res = "Fifteen"
            if self.p1points == 2:
                p1res = "Thirty"
            result = p1res + "-" + p2res
        return (result, p1res, p2res)

    def score(self):
        self.tied_score()
        if self.gamestate.result:
            return self.gamestate.result
        result, p1res, p2res = self.deuce()
        if result:
            return result
        gamestate = self.p1_has_points()
        gamestate = self.p2_has_points(gamestate)
        gamestate = self.p1_has_more_points(gamestate)
        result, p1res, p2res = self.p2_has_more_points(gamestate)


        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage player1"

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage player2"

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = "Win for player1"
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = "Win for player2"
        return result

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1
