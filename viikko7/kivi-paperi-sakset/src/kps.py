from tuomari import Tuomari

class KPS:
	def __init__(self) -> None:
		self._tuomari = Tuomari()

	def hae_siirrot(self):
		ekan_siirto = self._ensimmaisen_siirto()
		tokan_siirto = self._toisen_siirto()

		return (ekan_siirto, tokan_siirto)

	def pelaa(self):
		ekan_siirto, tokan_siirto = self.hae_siirrot()

		while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
			self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
			print(self._tuomari)

			ekan_siirto, tokan_siirto = self.hae_siirrot()

		print("Kiitos!")
		print(self._tuomari)

	def _ensimmaisen_siirto(self):
		return input("Ensimmäisen pelaajan siirto: ")

	def _toisen_siirto(self):
		return input("Toisen pelaajan siirto: ")

	def _onko_ok_siirto(self, siirto):
		return siirto == "k" or siirto == "p" or siirto == "s"