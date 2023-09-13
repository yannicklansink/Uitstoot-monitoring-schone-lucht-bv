# module_inspecteurs.py
import os

# This will automatically use the correct path seperator to support more OSs
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
INSPECTEURSBESTAND = os.path.join(CURRENT_DIRECTORY, "sample-files", "inspecteurs.txt")


lijst_inspecteurs = []  # lijst met alle inspecteur objecten


def lees_inspecteurs():
    """Inlezen van het tekstbestand met de inspecteursgegevens"""
    try:
        with open(INSPECTEURSBESTAND, mode="r") as inspecteurs:
            for record in inspecteurs:
                code = record[0:3]
                naam = record[4:24]
                standplaats = record[24:44]
                Inspecteur(code, naam, standplaats)
        print("Bestand", INSPECTEURSBESTAND, "ingelezen")
        return 0
    except FileNotFoundError:
        print("Bestand", INSPECTEURSBESTAND, "niet gevonden")
        return 1


def toon_inspecteurs():
    """Maak een overzicht van alle inspecteursgegevens"""
    print("Overzicht inspecteurs")
    print("=====================\n")
    for inspecteur in lijst_inspecteurs:
        inspecteur.toonGegevens()
        print("-" * 40)


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

    def toonGegevens(self):
        print(f"\tInspecteurscode: {self.__code}")
        print(f"\tNaam: {self.__naam}")
        print(f"\tStandplaats: {self.__standplaats}")
        # print(self.__code + " ", self.__naam, self.__standplaats)
