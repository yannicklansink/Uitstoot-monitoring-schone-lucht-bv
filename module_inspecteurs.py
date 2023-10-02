# module_inspecteurs.py
import os

# This will automatically use the correct path seperator to support more OSs
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
INSPECTEURSBESTAND = os.path.join(CURRENT_DIRECTORY, "sample-files", "inspecteurs.txt")
FILES_READ = set()

# lijst met alle inspecteur objecten
lijst_inspecteurs = []  


def lees_inspecteurs(file_name=INSPECTEURSBESTAND):
    """Inlezen van het tekstbestand met de inspecteursgegevens"""

    if file_name in FILES_READ:
        print(f"Bestand {file_name} is al ingelezen!")
        return

    try:
        with open(file_name, mode="r") as inspecteurs:
            for record in inspecteurs:
                code = record[0:3]
                naam = record[4:24]
                standplaats = record[24:44]
                Inspecteur(code, naam, standplaats)
        print("Bestand", file_name, "ingelezen")
        FILES_READ.add(file_name)
        return 0
    except FileNotFoundError:
        print("Bestand", file_name, "niet gevonden")
        return 1


def toon_inspecteurs():
    """Maak een overzicht van alle inspecteursgegevens"""
    if not is_lijst_inspecteurs_full():
        return
    print("Overzicht inspecteurs")
    print("=====================\n")
    for inspecteur in lijst_inspecteurs:
        inspecteur.toon_gegevens()
        print("-" * 40)


def toon_inspecteurs_code_en_naam():
    """Maak een overzicht van alle codes en namen van inspecteurs"""
    if not is_lijst_inspecteurs_full():
        return
    print("Overzicht inspecteurs")
    print("=====================\n")
    for inspecteur in lijst_inspecteurs:
        inspecteur.toon_code_en_naam()
        print("-" * 40)


def inspecteur_exists(code):
    """Check of een inspecteur met gegeven code bestaat"""
    if not is_lijst_inspecteurs_full():
        return
    for inspecteur in lijst_inspecteurs:
        if inspecteur.getCode() == code:
            return True
    return False


def is_lijst_inspecteurs_full():
    if not lijst_inspecteurs:
        print("Er zijn geen inspecteurs gevonden")
        return False
    return True


class Inspecteur:
    def __init__(self, code, naam="", standplaats=""):
        global lijst_inspecteurs

        self.__code = code
        self.__naam = naam
        self.__standplaats = standplaats
        self.__bezoekrapporten = []
        lijst_inspecteurs.append(self)

    def getCode(self):
        return self.__code

    def setCode(self, code):
        self.__code = code

    def getNaam(self):
        return self.__naam

    def setNaam(self, naam):
        self.__naam = naam

    def getStandplaats(self):
        return self.__standplaats

    def setStandplaats(self, standplaats):
        self.__standplaats = standplaats

    def addBezoekrapport(self, bezoekrapport):
        self.__bezoekrapporten.append(bezoekrapport)

    def toon_gegevens(self):
        print(f"\tInspecteurscode: {self.__code}")
        print(f"\tNaam: {self.__naam}")
        print(f"\tStandplaats: {self.__standplaats}")

    def toon_code_en_naam(self):
        print(f"\tInspecteurscode: {self.__code}")
        print(f"\tNaam: {self.__naam}")
