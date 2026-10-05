class Player:
    def __init__(self, name: str):
        self.points = 0
        self.result = ""
        self.name = name

    def __gt__(self, other):
        return self.points > other.points

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
        self._players_by_name = {
            player1_name: self.player1,
            player2_name: self.player2,
        }

    @property
    def highest_score(self):
        return max(self.player1, self.player2).points

    @property
    def lowest_score(self):
        return min(self.player1, self.player2).points

    @property
    def highest_result_string(self):
        return max(self.player1, self.player2).result

    @highest_result_string.setter
    def highest_result_string(self, new_result):
        max(self.player1, self.player2).result = new_result

    @property
    def lowest_result_string(self):
        return min(self.player1, self.player2).result

    @lowest_result_string.setter
    def lowest_result_string(self, new_result):
        min(self.player1, self.player2).result = new_result

    @property
    def highest_player_name(self):
        return max(self.player1, self.player2).name

    @property
    def lowest_player_name(self):
        return min(self.player1, self.player2).name

    def won_point(self, player_name):
        self._players_by_name[player_name].points += 1

    def tied_score(self):
        if self.player1.points == self.player2.points and self.player1.points < 3:
            self.result = self._lookup.get(self.player1.points, "")
            self.result += "-All"

    def deuce(self):
        if self.player1.points == self.player2.points and self.player1.points > 2:
            self.result = "Deuce"

    def one_player_has_more_points(self):
        if self.highest_score > self.lowest_score and self.highest_score < 4:
            self.highest_result_string = self._lookup.get(self.highest_score, "")
            self.lowest_result_string = self._lookup.get(self.lowest_score, "")
            self.result = self.player1.result + "-" + self.player2.result

    def one_player_has_advantage(self):
        if self.highest_score > self.lowest_score and self.lowest_score >= 3 and (self.highest_score - self.lowest_score) < 2:
            self.result = f"Advantage {self.highest_player_name}"

    def one_player_wins(self):
        if (
            self.highest_score >= 4
            and self.lowest_score >= 0
            and (self.highest_score - self.lowest_score) >= 2
        ):
            self.result = f"Win for {self.highest_player_name}"

    def score(self):
        self.tied_score()
        self.deuce()
        self.one_player_has_more_points()
        self.one_player_has_advantage()
        self.one_player_wins()
        return self.result


# for next time: use bit patterns to determine which action, each condition (eg self.highest_score > self.lowest_score) is binary