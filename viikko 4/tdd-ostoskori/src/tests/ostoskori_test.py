import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Keksi", 1))

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 4)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        #Testaa että sama olio
        self.assertEqual(maito, ostos.tuote)    
        self.assertEqual("Maito", ostos.tuote.nimi())
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota_joilla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        nakki = Tuote("Nakki", 1)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(nakki)

        ostoskori = self.kori.ostokset()

        self.assertEqual(len(ostoskori), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota_joilla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostoskori = self.kori.ostokset()

        self.assertEqual(len(ostoskori), 1)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(maito, ostos.tuote)    
        self.assertEqual("Maito", ostos.tuote.nimi())
        self.assertEqual(ostos.lukumaara(), 2)

    def test_korissa_kaksi_samaa_tuotetta_joista_toinen_poistetaan_muuttaa_lukumaaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostoskori = self.kori.ostokset()

        self.assertEqual(len(ostoskori), 1)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 2)

        self.kori.poista_tuote(maito)
        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.lukumaara(), 1)

    def test_korissa_yksi_tuote_joka_poistetaan_ostoskori_tyhjenee(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostoskori = self.kori.ostokset()
        self.assertEqual(len(ostoskori), 1)

        self.kori.poista_tuote(maito)
        ostoskori = self.kori.ostokset()
        self.assertEqual(len(ostoskori), 0)

        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)

    def test_tyhjenna_tyhjentaa_ostoskorin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostoskori = self.kori.ostokset()
        self.assertEqual(len(ostoskori), 1)

        self.kori.tyhjenna()
        ostoskori = self.kori.ostokset()
        self.assertEqual(len(ostoskori), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)