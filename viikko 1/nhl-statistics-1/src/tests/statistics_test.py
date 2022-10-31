import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_bad_init(self):
      # Test bad init without argument raises TypeError
      with self.assertRaises(TypeError):
        Statistics()
    
    def test_search_no_name_found(self):
      #Test search returns None if no player that name was found.
      found = self.statistics.search("Testi")
      self.assertIsNone(found)

    def test_search_name_found(self):
      #Test search return matches expected
      found = self.statistics.search("Semenko")
      assert isinstance(found, object)

      self.assertEqual(found.name, "Semenko")
      self.assertEqual(found.team, "EDM")
      self.assertEqual(found.goals, 4)
      self.assertEqual(found.assists, 12)

    def test_team_players_not_found_returns_empty(self):
      found = self.statistics.team("ASD")
      assert isinstance(found, list)
      self.assertEqual(found, [])

    def test_team_players_found(self):
      found = self.statistics.team("EDM")

      assert isinstance(found, list)
      self.assertEqual(len(found), 3)

    def test_top_players_with_zero_given(self):
      found = self.statistics.top(0)
      self.assertEqual(found, [])

    def test_top_players(self):
      found = self.statistics.top(3)
      self.assertEqual(len(found), 3)

    def test_top_players_when_given_larger_number_than_players(self):
      found = self.statistics.top(1000)
      self.assertEqual(len(found), 5)

    
