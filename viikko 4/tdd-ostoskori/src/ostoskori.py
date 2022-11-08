from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset_korissa = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        lukumaara = 0
        for ostos in self.ostokset_korissa.values():
            lukumaara += ostos.lukumaara()
        
        return lukumaara

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0
        for ostos in self.ostokset_korissa.values():
            hinta += ostos.hinta()
        
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if lisattava.nimi() in self.ostokset_korissa:
            self.ostokset_korissa[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            lisattava_ostos = Ostos(lisattava)
            self.ostokset_korissa[lisattava.nimi()] = lisattava_ostos

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        if poistettava.nimi() in self.ostokset_korissa:
            self.ostokset_korissa[poistettava.nimi()].muuta_lukumaaraa(-1)

            if self.ostokset_korissa[poistettava.nimi()].lukumaara() == 0:
                 del self.ostokset_korissa[poistettava.nimi()]

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.ostokset_korissa = {}

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return [ostos for ostos in self.ostokset_korissa.values()]