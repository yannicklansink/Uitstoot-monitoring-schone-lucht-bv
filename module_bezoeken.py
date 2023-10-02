import os
from module_inspecteurs import lijst_inspecteurs
from module_bedrijven import lijst_bedrijven
from datetime import datetime, date, MINYEAR, MAXYEAR

# This will automatically use the correct path seperator to support more OSs
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
BEZOEKENBESTAND = os.path.join(CURRENT_DIRECTORY, "sample-files", "bezoekrapporten.txt")
FILES_READ = set()

# lijst met alle rapporten
lijst_rapporten = []  


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

            print(f"Bezoekrapporten uit {file_name} ingelezen")
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
            inspecteur.toon_gegevens()
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


def toon_rapport_by_bedrijf(
    bedrijfscode, begin_datum=date(MINYEAR, 1, 1), eind_datum=date(MAXYEAR, 1, 1)
):
    """Overzicht tonen van alle bezoekrapporten van een bedrijf met mogelijk een begin- en einddatum aflopend gesorteerd op datum"""
    lijst_met_bezoeken_per_bedrijf = []

    for bezoek in lijst_rapporten:
        if bezoek.get_bedrijfscode() == bedrijfscode:
            try:
                bezoekdatum = datetime.strptime(
                    bezoek.get_bezoekdatum(), "%d-%m-%Y"
                ).date()
            except ValueError:
                print("Kon de bezoekdatum niet converteren naar een date")
            if begin_datum <= bezoekdatum <= eind_datum:
                lijst_met_bezoeken_per_bedrijf.append(bezoek)

    # Sorteer de lijst gebaseerd op de bezoekdatum
    lijst_met_bezoeken_per_bedrijf.sort(
        key=lambda x: datetime.strptime(x.get_bezoekdatum(), "%d-%m-%Y"), reverse=True
    )

    if not lijst_met_bezoeken_per_bedrijf:
        print("Er zijn geen bezoeksrapporten gevonden van het bedrijf:", bedrijfscode)
        print("In de periode van", begin_datum, "|", eind_datum)
        return

    for bezoek_van_bedrijf in lijst_met_bezoeken_per_bedrijf:
        print()
        print("\tBedrijfs info:", bezoek_van_bedrijf.get_bedrijfscode())
        inspecteur = bezoek_van_bedrijf.get_inspecteur_by_code(
            bezoek_van_bedrijf._Bezoek__inspecteurscode
        )
        if inspecteur:
            print("\tInspecteursnaam:", inspecteur.getNaam())
        else:
            print("\tInspecteurscode:", bezoek_van_bedrijf._Bezoek__inspecteurscode)
        bezoek_van_bedrijf.toon_gegevens()


def toon_rapport_by_inspecteur(
    inspecteurscode, begin_datum=date(MINYEAR, 1, 1), eind_datum=date(MAXYEAR, 1, 1)
):
    """Overzicht tonen van alle bezoekrapporten van een inspecteur met mogelijk een begin- en einddatum aflopend gesorteerd op datum"""
    lijst_met_bezoeken_per_inspecteur = []

    for bezoek in lijst_rapporten:
        if bezoek.get_inspecteurscode() == inspecteurscode:
            try:
                bezoekdatum = datetime.strptime(
                    bezoek.get_bezoekdatum(), "%d-%m-%Y"
                ).date()
            except ValueError:
                print("Kon de bezoekdatum niet converteren naar een date")
            if begin_datum <= bezoekdatum <= eind_datum:
                lijst_met_bezoeken_per_inspecteur.append(bezoek)

    # Sorteer de lijst gebaseerd op de bezoekdatum
    lijst_met_bezoeken_per_inspecteur.sort(
        key=lambda x: datetime.strptime(x.get_bezoekdatum(), "%d-%m-%Y"), reverse=True
    )

    if not lijst_met_bezoeken_per_inspecteur:
        print(
            "Er zijn geen bezoeksrapporten gevonden van de inspecteur:", inspecteurscode
        )
        print("In de periode van", begin_datum, "|", eind_datum)
        return

    for bezoek_van_inspecteur in lijst_met_bezoeken_per_inspecteur:
        print()
        print("\tInspecteurs info:", bezoek_van_inspecteur.get_inspecteurscode())
        bedrijf = bezoek_van_inspecteur.get_bedrijf_by_code(
            bezoek_van_inspecteur._Bezoek__bedrijfscode
        )
        if bedrijf:
            print("\tBedrijfsnaam:", bedrijf.get_naam())
        else:
            print("\tBedrijfscode:", bezoek_van_inspecteur._Bezoek__bedrijfscode)
        bezoek_van_inspecteur.toon_gegevens()


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

    def get_inspecteurscode(self):
        return self.__inspecteurscode

    def get_bedrijfscode(self):
        return self.__bedrijfscode

    def get_bezoekdatum(self):
        return self.__bezoekdatum

    def toon_gegevens(self):
        print(f"\tBezoekdatum: {self.__bezoekdatum}")
        print(f"\tDatum_opstellen_rapport: {self.__datum_opstellen_rapport}")
        print(f"\tStatus: {self.__status}")
        print(f"\tOpmerking: {self.__opmerking}")
