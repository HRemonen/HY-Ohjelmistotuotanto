from kps_tekoaly import KPSTekoaly
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPSTekoaly):
	def __init__(self) -> None:
		super().__init__()
		self._tekoaly = TekoalyParannettu(10)

	def _toisen_siirto(self):
		siirto = self._tekoaly.anna_siirto()
		print(f"Tietokone valitsi: {siirto}")
		self._tekoaly.aseta_siirto(siirto)

		return siirto