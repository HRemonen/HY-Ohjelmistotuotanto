def validoi_kokonaisluku(luku):
    if not isinstance(luku, int):
        raise Exception("Annettujen arvojen pitää olla kokonaislukuja")
    if luku < 0:
        raise Exception("Annettujen arvojen pitää olla positiivisia kokonaislukuja")
    
    return luku

class IntJoukko:
    def __init__(self, kapasiteetti = 5, kasvatuskoko = 5):
        self.kapasiteetti = validoi_kokonaisluku(kapasiteetti)
        self.kasvatuskoko = validoi_kokonaisluku(kasvatuskoko)

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kasvata_kokoa(self):
        self.lukujono += [0] * self.kasvatuskoko

    def kuuluu(self, tarkistettava_luku):
        for luku in self.lukujono:
            if luku == tarkistettava_luku:
                return True
        return False

    def lisaa(self, luku):
        if self.kuuluu(luku):
            return False

        elif self.alkioiden_lkm == 0:
            self.lukujono[0] = luku
            self.alkioiden_lkm += 1
            return True
        
        self.lukujono[self.alkioiden_lkm] = luku
        self.alkioiden_lkm += 1

        if len(self.lukujono) == self.alkioiden_lkm:
            self.kasvata_kokoa()
            return True

        return False

    def poista(self, luku):
        try:
            poistettavan_indeksi = self.lukujono.index(luku)
            del self.lukujono[poistettavan_indeksi]
            self.alkioiden_lkm -= 1
            return True

        except Exception:
            return False

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        return self.lukujono[: self.alkioiden_lkm]

    @staticmethod
    def yhdiste(a, b):
        yhdistetty_lista = IntJoukko()
        apulista = a.to_int_list() + b.to_int_list()

        for alkio in apulista:
            yhdistetty_lista.lisaa(alkio)

        return yhdistetty_lista

    @staticmethod
    def leikkaus(a, b):
        leikkaus_lista = IntJoukko()
        a_taulu = a.to_int_list()

        for alkio in a_taulu:
            if b.kuuluu(alkio):
                leikkaus_lista.lisaa(alkio)

        return leikkaus_lista

    @staticmethod
    def erotus(a, b):
        erotus_lista = IntJoukko()
        a_taulu = a.to_int_list()

        for alkio in a_taulu:
            if not b.kuuluu(alkio):
                erotus_lista.lisaa(alkio)

        return erotus_lista

    def __str__(self):
        joukon_alkiot = self.to_int_list()
        return '{' + f"{', '.join(str(alkio) for alkio in joukon_alkiot)}" + "}"
       
