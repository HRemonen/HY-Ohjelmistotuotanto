from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Not, Or, HasAtLeast, HasFewerThan, PlaysIn

def print_players(stats, matcher):
    for player in stats.matches(matcher):
        print(player)

    print()

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    print_players(stats, matcher)

    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    print_players(stats, matcher)

    matcher = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    print_players(stats, matcher)

    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    print_players(stats, matcher)

if __name__ == "__main__":
    main()
