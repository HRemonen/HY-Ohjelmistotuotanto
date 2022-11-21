from kps import KPS
from tekoaly import Tekoaly

class KPSTekoaly(KPS):
	def __init__(self) -> None:
		super().__init__()
		self._tekoaly = Tekoaly()

	def _toisen_siirto(self):
		siirto = self._tekoaly.anna_siirto()
		print(f"Tietokone valitsi: {siirto}")
		
		return siirto
