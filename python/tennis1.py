class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1points += 1
        else:
            self.p2points += 1

    def equal_points(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.p1points, "Deuce")
        return result

    def four_or_more_points(self):
        point_difference = self.p1points - self.p2points
        player_name = "player1" if point_difference > 0 else "player2"
        score = "Advantage" if abs(point_difference) == 1 else "Win for"

        return f"{score} {player_name}"

    def normie_scores(self):
        mapping = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
        }
        result = f"{mapping[self.p1points]}-{mapping[self.p2points]}"
        return result


    def score(self):
        if self.p1points == self.p2points:
            return self.equal_points()
        elif self.p1points >= 4 or self.p2points >= 4:
            return self.four_or_more_points()
        else:
            return self.normie_scores()
