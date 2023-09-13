import os
from module_inspecteurs import lijst_inspecteurs
from module_bedrijven import lijst_bedrijven

# This will automatically use the correct path seperator to support more OSs
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
BEZOEKENBESTAND = os.path.join(CURRENT_DIRECTORY, "sample-files", "bezoekrapporten.txt")
FILES_READ = set()

lijst_rapporten = []  # lijst met alle rapporten


def lees_rapporten(file_name=BEZOEKENBESTAND):
    """Inlezen van het tekstbestand met bezoekrapporten"""

    if file_name in FILES_READ:
        print(f"Bestand {file_name} is al ingelezen!")
        return

    try:
        with open(file_name, "r") as file:
            for line in file:
                inspecteurscode = line[0:3].strip()
                bedrijfscode = line[4:8].strip()
                bezoekdatum = line[9:19].strip() or None
                datum_opstellen_rapport = line[20:30].strip() or None
                status = line[31:42].strip() or None
                opmerking = line[42:-2].strip() or None

                Bezoek(
                    inspecteurscode,
                    bedrijfscode,
                    bezoekdatum,
                    datum_opstellen_rapport,
                    status,
                    opmerking,
                )
                
            print(f"Bezoekrapporten uit {file_name} ingelezen!")
            FILES_READ.add(file_name)

    except FileNotFoundError:
        print(f"Bestand {file_name} niet gevonden!")


def toon_rapporten():
    """Overzicht tonen van alle bezoeksrapporten en daaraan gekoppeld bedrijf en inspecteur"""
    print("lengte lijst rapporten: ", len(lijst_rapporten))
    for rapport in lijst_rapporten:
        inspecteur = rapport.get_inspecteur_by_code(rapport._Bezoek__inspecteurscode)
        if inspecteur:
            print("inspecteurs info:")
            inspecteur.toonGegevens()
        else:
            print("Inspecteurscode:", rapport._Bezoek__inspecteurscode)

        bedrijf = rapport.get_bedrijf_by_code(rapport._Bezoek__bedrijfscode)
        if bedrijf:
            print("bedrijf info:")
            bedrijf.toonGegevens()
        else:
            print("Bedrijfscode:", rapport._Bezoek__bedrijfscode)

        print("Bezoekdatum:", rapport._Bezoek__bezoekdatum)
        print("Datum Opstellen Rapport:", rapport._Bezoek__datum_opstellen_rapport)
        print("Status:", rapport._Bezoek__status)
        print("Opmerking:", rapport._Bezoek__opmerking)
        print("=" * 40 + "\n")


class Bezoek:
    def __init__(
        self,
        inspecteurscode,
        bedrijfscode,
        bezoekdatum,
        datum_opstellen_rapport,
        status,
        opmerking,
    ):
        global lijst_rapporten
        self.__inspecteurscode = inspecteurscode
        self.__bedrijfscode = bedrijfscode
        self.__bezoekdatum = bezoekdatum
        self.__datum_opstellen_rapport = datum_opstellen_rapport
        self.__status = status
        self.__opmerking = opmerking

        lijst_rapporten.append(self)

    def get_inspecteur_by_code(self, inspecteurscode):
        """Get inspecteur met specifieke inspecteurscode"""
        for inspecteur in lijst_inspecteurs:
            if inspecteur.getCode() == inspecteurscode:
                return inspecteur

    def get_bedrijf_by_code(self, bedrijfscode):
        """Get bedrijf met specifieke bedrijfscode"""
        for bedrijf in lijst_bedrijven:
            if bedrijf.getCode() == bedrijfscode:
                return bedrijf
