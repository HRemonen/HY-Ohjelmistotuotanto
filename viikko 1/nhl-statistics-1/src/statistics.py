from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

class Statistics:
    def __init__(self, reader):
        self.reader = reader

        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, f = SortBy.POINTS):
        if f.value == 1:
            sortby = lambda x : x.points
        elif f.value == 2:
            sortby = lambda x : x.goals
        else:
            sortby = lambda x : x.assists

        if how_many > len(self._players):
            how_many = len(self._players)

        sorted_players = sorted(
            self._players,
            reverse=True,
            key = sortby
        )

        result = []
        i = 0
        while i < how_many:
            result.append(sorted_players[i])
            i += 1

        return result
