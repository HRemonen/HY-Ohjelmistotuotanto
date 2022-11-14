class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = [tulos]

    def miinus(self, arvo):
        uusi_arvo = self.laskimen_arvo() - arvo
        self.aseta_arvo(uusi_arvo)

    def plus(self, arvo):
        uusi_arvo = self.laskimen_arvo() + arvo
        self.aseta_arvo(uusi_arvo)

    def nollaa(self):
        self.tulos = [0]

    def aseta_arvo(self, arvo):
        self.tulos.append(arvo)

    def kumoa(self):
        self.tulokset.pop()
    
    def laskimen_arvo(self):
        return self.tulos[-1]

    @property
    def tulokset(self):
        return self.tulos
