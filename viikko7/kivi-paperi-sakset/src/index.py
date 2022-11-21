from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Tehdas:
    @staticmethod
    def uusi_p_vs_p():
        return KPSPelaajaVsPelaaja()
    
    @staticmethod
    def uusi_ai_vs_p():
        return KPSTekoaly()

    @staticmethod
    def uusi_parempiAI_vs_p():
        return KPSParempiTekoaly()

def aloitus(peli):
    print(
        "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
    )
    peli.pelaa()

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus.endswith("a"):
            aloitus(Tehdas.uusi_p_vs_p())
            
        elif vastaus.endswith("b"):
            aloitus(Tehdas.uusi_ai_vs_p())

        elif vastaus.endswith("c"):
            aloitus(Tehdas.uusi_parempiAI_vs_p())

        else:
            break

if __name__ == "__main__":
    main()
