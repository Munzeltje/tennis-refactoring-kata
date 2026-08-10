class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def won_point(self):
        self.points += 1


class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.won_point()
        else:
            self.player2.won_point()

    def equal_points(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.player1.points, "Deuce")
        return result

    def four_or_more_points(self):
        point_difference = self.player1.points - self.player2.points
        player_name = self.player1.name if point_difference > 0 else self.player2.name
        score = "Advantage" if abs(point_difference) == 1 else "Win for"

        return f"{score} {player_name}"

    def normie_scores(self):
        mapping = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        result = f"{mapping[self.player1.points]}-{mapping[self.player2.points]}"
        return result


    def score(self):
        if self.player1.points == self.player2.points:
            return self.equal_points()
        elif self.player1.points >= 4 or self.player2.points >= 4:
            return self.four_or_more_points()
        else:
            return self.normie_scores()
