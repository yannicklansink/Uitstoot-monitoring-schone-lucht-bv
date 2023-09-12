import os

# This will automatically use the correct path seperator to support more OSs
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
BEDRIJFSBESTAND = os.path.join(CURRENT_DIRECTORY, "sample-files", "bedrijven.txt")

lijst_bedrijven = []  # lijst met alle bedrijven


def lees_bedrijven():
    """Inlezen van het tekstbestand met bedrijfsgegevens"""
    try:
        with open(BEDRIJFSBESTAND, "r") as file:
            for line in file:
                # Splitting attributes based on the structure of the bedrijven.txt file
                attrs = [
                    line[0:3].strip(),
                    line[5:20].strip(),
                    line[25:54].strip(),
                    line[54:64].strip(),
                    line[64:85].strip(),
                    line[85:88].strip(),
                    line[88:91].strip(),
                    line[91:101].strip(),
                    line[101:111].strip(),
                    line[111:121].strip(),
                    line[121:124].strip(),
                    line[124:126].strip(),
                    # line[126:150].strip(),
                ]
                bedrijf = Bedrijf(*attrs)
            print("Bestand", BEDRIJFSBESTAND, "ingelezen")
    except FileNotFoundError:
        print("Bestand", BEDRIJFSBESTAND, "niet gevonden")
        return 1


def toon_bedrijven():
    """Overzicht tonen van alle bedrijven"""
    print("Overzicht bedrijven")
    print("=====================\n")
    for bedrijf in lijst_bedrijven:
        bedrijf.toonGegevens()
        print("-" * 40)


class Bedrijf:
    def __init__(
        self,
        code=None,
        naam=None,
        straat=None,
        huisnummer=None,
        postcode=None,
        plaats=None,
        breedtegraad=None,
        lengtegraad=None,
        max_toegestande_uitstoot=None,
        berekende_uitstoot=None,
        boete=None,
        controle=None,
        inspectie_frequentie=None,
        contactpersoon=None,
    ):
        global lijst_bedrijven
        self.__code = code
        self.__naam = naam
        self.__straat = straat
        self.__huisnummer = huisnummer
        self.__postcode = postcode
        self.__plaats = plaats
        self.__breedtegraad = breedtegraad
        self.__lengtegraad = lengtegraad
        self.__max_toegestande_uitstoot = max_toegestande_uitstoot
        self.__berekende_uitstoot = berekende_uitstoot
        self.__boete = boete
        self.__controle = controle
        self.__inspectie_frequentie = inspectie_frequentie
        self.__contactpersoon = contactpersoon

        lijst_bedrijven.append(self)

    def toonGegevens(self):
        print(f"Code: {self.__code}")
        print(f"Naam: {self.__naam}")
        print(f"Straat: {self.__straat} {self.__huisnummer}")
        print(f"Postcode: {self.__postcode}")
        print(f"Plaats: {self.__plaats}")
        print(f"Breedtegraad: {self.__breedtegraad}")
        print(f"Lengtegraad: {self.__lengtegraad}")
        print(f"Max Toegestande Uitstoot: {self.__max_toegestande_uitstoot}")
        print(f"Berekende Uitstoot: {self.__berekende_uitstoot}")
        print(f"Boete: {self.__boete}")
        print(f"Controle: {self.__controle}")
        print(f"Inspectie Frequentie: {self.__inspectie_frequentie}")
        print(f"Contactpersoon: {self.__contactpersoon}")
        print("---------------------\n")
