class PlayerStats:
	def __init__(self, reader) -> None:
		self.player_reader = reader

	def top_scorers_by_nationality(self, nationality):
		players = self.player_reader.get_players(nationality)
		
		return sorted(players, key=lambda x: x.points, reverse=True)