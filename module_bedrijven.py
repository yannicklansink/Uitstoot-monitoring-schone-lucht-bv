import os
import numpy as np
import matplotlib.pyplot as plt
import module_metingen as metingen

# This will automatically use the correct path seperator to support more OSs
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
BEDRIJFSBESTAND = os.path.join(CURRENT_DIRECTORY, "sample-files", "bedrijven.txt")

FILES_READ = set()

C1 = 1  # CO2
C2 = 25  # CH4
C3 = 5  # NO2
C4 = 1000  # NH3

BOETE_FACTOR = 1

lijst_bedrijven = []  # lijst met alle bedrijven


def lees_bedrijven(file_name=BEDRIJFSBESTAND):
    """Inlezen van het tekstbestand met bedrijfsgegevens"""

    if file_name in FILES_READ:
        print(f"Bestand {file_name} is al ingelezen!")
        return

    try:
        with open(file_name, "r") as file:
            for line_num, line in enumerate(file, 1):
                if not line.endswith(".\n"):
                    print(f"Line {line_num} doesn't end with the expected marker.")
                    continue

                try:
                    # Splitting fields
                    code = line[0:5].strip()
                    naam = line[5:25].strip()
                    straat = line[25:55].strip()
                    huisnummer = line[54:57].strip()
                    postcode = line[57:67].strip()
                    plaats = line[67:85].strip()
                    breedtegraad = line[85:89].strip()
                    lengtegraad = line[89:93].strip()
                    max_toegestande_uitstoot = line[93:101].strip()
                    berekende_uitstoot = line[101:111].strip()
                    boete = (
                        line[111:121].strip() if "nan" not in line[111:121] else None
                    )
                    controle = line[135:139].strip()
                    inspectie_frequentie = line[139:142].strip()
                    contactpersoon = line[142:160].strip() if controle == "ja" else None

                    bedrijf = Bedrijf(
                        code,
                        naam,
                        straat,
                        huisnummer,
                        postcode,
                        plaats,
                        breedtegraad,
                        lengtegraad,
                        max_toegestande_uitstoot,
                        berekende_uitstoot if "nan" not in berekende_uitstoot else None,
                        boete,
                        controle,
                        inspectie_frequentie,
                        contactpersoon,
                    )

                except IndexError:
                    print(f"Line {line_num} in the file is shorter than expected.")
                except ValueError as e:
                    print(f"Error processing line {line_num}: {e}")

            print("Bestand", file_name, "ingelezen")
            FILES_READ.add(file_name)

    except FileNotFoundError:
        print("Bestand", file_name, "niet gevonden")
        return 1


def toon_bedrijven():
    """Overzicht tonen van alle bedrijven"""
    if not is_lijst_bedrijven_full():
        return

    print("Overzicht bedrijven")
    print("=====================\n")
    for bedrijf in lijst_bedrijven:
        bedrijf.toonGegevens()
        print("-" * 40)


def bereken_bedrijven_uitstoot():
    if not is_lijst_bedrijven_full():
        return

    for bedrijf in lijst_bedrijven:
        x, y = int(bedrijf.getBreedtegraad()), int(bedrijf.getLengtegraad())

        # Calculate the weighted uitstoot
        weighted_uitstoot = 0

        for i in range(-2, 3):  # This will loop from -2 to 2
            for j in range(-2, 3):
                if 0 <= x + i < 100 and 0 <= y + j < 100:  # Check bounds
                    if i == 0 and j == 0:
                        gas1 = bedrijf.getUitstootGas1(x, y)
                        gas2 = bedrijf.getUitstootGas2(x, y)
                        gas3 = bedrijf.getUitstootGas3(x, y)
                        gas4 = bedrijf.getUitstootGas4(x, y)

                        uitstoot1m2 = C1 * gas1 + C2 * gas2 + C3 * gas3 + C4 * gas4
                        weighted_uitstoot += uitstoot1m2
                    elif abs(i) == 2 or abs(j) == 2:
                        # 16X | 2de ring
                        gas1 = bedrijf.getUitstootGas1(x + i, y + j)
                        gas2 = bedrijf.getUitstootGas2(x + i, y + j)
                        gas3 = bedrijf.getUitstootGas3(x + i, y + j)
                        gas4 = bedrijf.getUitstootGas4(x + i, y + j)

                        uitstoot1m2 = C1 * gas1 + C2 * gas2 + C3 * gas3 + C4 * gas4
                        weighted_uitstoot += uitstoot1m2 * 0.25
                    else:
                        # 8x | 1e ring
                        gas1 = bedrijf.getUitstootGas1(x + i, y + j)
                        gas2 = bedrijf.getUitstootGas2(x + i, y + j)
                        gas3 = bedrijf.getUitstootGas3(x + i, y + j)
                        gas4 = bedrijf.getUitstootGas4(x + i, y + j)

                        uitstoot1m2 = C1 * gas1 + C2 * gas2 + C3 * gas3 + C4 * gas4
                        weighted_uitstoot += uitstoot1m2 * 0.5

        # Set this computed value to the bedrijf object
        bedrijf.setBerekendeUitstoot(format(weighted_uitstoot, ".2f"))


def bereken_bedrijven_boete():
    for bedrijf in lijst_bedrijven:
        bedrijf.berekenBoete()


def is_lijst_bedrijven_full():
    if not lijst_bedrijven:
        print("Er zijn geen bedrijven gevonden")
        return False
    return True


def toon_bedrijven_code_en_naam():
    """Maak een overzicht van alle codes en namen van bedrijven"""
    if not is_lijst_bedrijven_full():
        return
    print("Overzicht bedrijven")
    print("=====================\n")
    for bedrijf in lijst_bedrijven:
        bedrijf.toon_code_en_naam()
        print("-" * 40)


def bedrijf_exists(code):
    """Check of een bedrijf met gegeven code bestaat"""
    if not is_lijst_bedrijven_full():
        return
    for bedrijf in lijst_bedrijven:
        if bedrijf.getCode() == code:
            return True
    return False


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
        max_toegestaande_uitstoot=None,
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
        self.__max_toegestaande_uitstoot = max_toegestaande_uitstoot
        self.__berekende_uitstoot = berekende_uitstoot
        self.__boete = boete
        self.__controle = controle
        self.__inspectie_frequentie = inspectie_frequentie
        self.__contactpersoon = contactpersoon

        lijst_bedrijven.append(self)

    def toonGegevens(self):
        print(f"\tBedrijfscode: {self.__code}")
        print(f"\tNaam: {self.__naam}")
        print(f"\tStraat: {self.__straat}")
        print(f"\tHuisnummer: {self.__huisnummer}")
        print(f"\tPostcode: {self.__postcode}")
        print(f"\tPlaats: {self.__plaats}")
        print(f"\tBreedtegraad: {self.__breedtegraad}")
        print(f"\tLengtegraad: {self.__lengtegraad}")
        print(f"\tMax Toegestaande Uitstoot: {self.__max_toegestaande_uitstoot}")
        print(f"\tBerekende Uitstoot: {self.__berekende_uitstoot}")
        print(f"\tBoete: {self.__boete}")
        print(f"\tControle: {self.__controle}")
        print(f"\tInspectie Frequentie: {self.__inspectie_frequentie}")
        print(f"\tContactpersoon: {self.__contactpersoon}")

    def getCode(self):
        return self.__code

    def get_naam(self):
        return self.__naam

    def getBreedtegraad(self):
        return self.__breedtegraad

    def getLengtegraad(self):
        return self.__lengtegraad

    def getUitstootGas1(self, breedtegraad, lengtegraad):
        gas = metingen.get_uitstoot_gas_CO2(breedtegraad, lengtegraad)
        return gas

    def getUitstootGas2(self, breedtegraad, lengtegraad):
        gas = metingen.get_uitstoot_gas_CH4(breedtegraad, lengtegraad)
        return gas

    def getUitstootGas3(self, breedtegraad, lengtegraad):
        gas = metingen.get_uitstoot_gas_NO2(breedtegraad, lengtegraad)
        return gas

    def getUitstootGas4(self, breedtegraad, lengtegraad):
        gas = metingen.get_uitstoot_NH3(breedtegraad, lengtegraad)
        return gas

    def setBerekendeUitstoot(self, berekende_uitstoot):
        self.__berekende_uitstoot = berekende_uitstoot

    def getMaxToegestaandeUitstoot(self):
        return self.__max_toegestaande_uitstoot

    def berekenBoete(self):
        if float(self.__berekende_uitstoot) > float(self.__max_toegestaande_uitstoot):
            self.__boete = format(
                (
                    float(self.__berekende_uitstoot)
                    - float(self.__max_toegestaande_uitstoot)
                )
                * BOETE_FACTOR,
                ".2f",
            )
            print(
                "\t",
                self.__naam,
                "heeft de volgende boete gekregen:",
                self.__boete,
                "\n\t",
                "door een berekende uitstoot van:",
                self.__berekende_uitstoot,
                "\n",
            )
        else:
            self.__boete = 0

    def toon_code_en_naam(self):
        print(f"\tBedrijfscode: {self.__code}")
        print(f"\tNaam: {self.__naam}")
