SCORES = ["Love", "Fifteen", "Thirty", "Forty", "Deuce"]

class Player:
    def __init__(self, name) -> None:
        self.name = name
        self._points = 0

    def won_game(self):
        self._points += 1

    @property
    def points(self):
        return self._points
    
    def __str__(self) -> str:
        return f"{self.name} {SCORES[self._points]}"

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {
            player1_name: Player(player1_name),
            player2_name: Player(player2_name)
        }
        self.player1 = player1_name
        self.player2 = player2_name

    def won_point(self, player_name):
        player = self.players[player_name]
        player.won_game()

    def get_score(self):
        player1 = self.players[self.player1].points
        player2 = self.players[self.player2].points
        difference = player1 - player2

        if player1 < 4 and player2 < 4:
            if player1 == player2:
                return f"{SCORES[player1]}-All"
            return f"{SCORES[player1]}-{SCORES[player2]}"
        
        elif player1 >= 4 or player2 >= 4:
            if difference == 0:
                return "Deuce"
            elif difference == 1:
                return "Advantage player1"
            elif difference == -1:
                return "Advantage player2"
            elif difference >= 2:
                return "Win for player1"
            else:
                return "Win for player2"


