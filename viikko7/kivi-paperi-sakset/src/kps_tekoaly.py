from kps import KPS
from tekoaly import Tekoaly

class KPSTekoaly(KPS):
	def __init__(self) -> None:
		self._tekoaly = Tekoaly()

	def _toisen_siirto(self, ensimmaisen_siirto):
		return self._tekoaly.anna_siirto(ensimmaisen_siirto)
