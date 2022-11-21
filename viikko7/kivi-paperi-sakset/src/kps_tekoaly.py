from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly:
	def __init__(self) -> None:
		self._tekoaly = Tekoaly()

	def _toisen_siirto(self, ensimmaisen_siirto):
		return self._tekoaly.anna_siirto(ensimmaisen_siirto)
