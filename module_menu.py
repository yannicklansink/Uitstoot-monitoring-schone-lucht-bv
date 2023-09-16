import module_inspecteurs as mi
import module_metingen as mm
import module_bedrijven as bedrijven
import module_bezoeken as rapporten
from datetime import datetime


def handle_bezoeksrapport_keuze():
    print("1. Overzicht alle bezoeksrapporten")
    print("2. Overzicht bezoeksrapport per inspecteur")
    print("3. Overzicht bezoeksrapport per bedrijf")
    print("0. stoppen\n")
    try:
        bezoeksrapport_keuze = int(input("Uw keuze : "))
    except ValueError:
        print("Ongeldige invoer. Probeer opnieuw.")
        return

    if bezoeksrapport_keuze == 1:
        rapporten.toon_rapporten()
    elif bezoeksrapport_keuze == 2:
        try:
            if not mi.is_lijst_inspecteurs_full():
                return
            mi.toon_inspecteurs_code_en_naam()
            inspecteurs_keuze = input("Kies de inspecteurscode: ")
            if not mi.inspecteur_exists(inspecteurs_keuze):
                print("De inspecteur code is niet gevonden")
                return
        except:
            print("Ongeldige invoer. Probeer opnieuw.")
            return
        # check of de gebruiker nog een begin- en einddatum wilt invullen
        try:
            incorrect_antwoord = True
            while incorrect_antwoord:
                begin_of_einddatum = input(
                    "Wil je nog een begin- en einddatum invullen? (y)/(n): "
                )
                begin_of_einddatum = begin_of_einddatum.lower()
                if begin_of_einddatum != "y" and begin_of_einddatum != "n":
                    print("Kies 'y' of 'n'")
                else:
                    incorrect_antwoord = False
            if begin_of_einddatum == "n":
                rapporten.toon_rapport_by_inspecteur(inspecteurs_keuze)
            else:
                gekozen_begin_datum = get_date_input(
                    "Kies een begin datum: (YYYY-MM-DD)"
                )
                gekozen_eind_datum = get_date_input("Kies een eind datum: (YYYY-MM-DD)")
                rapporten.toon_rapport_by_inspecteur(
                    inspecteurs_keuze, gekozen_begin_datum, gekozen_eind_datum
                )
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw.")
            return

    elif bezoeksrapport_keuze == 3:
        rapporten.toon_rapport_by_bedrijf()
    elif keuze == 0:
        return
    else:
        print("ongeldige keuze")
        return


def get_date_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            valid_date = datetime.strptime(user_input, "%Y-%m-%d").date()
            return valid_date
        except ValueError:
            print("Verkeerd geformateerd. Gebruik het volgende formaat YYYY-MM-DD.")


# start applicatie
while True:
    print("\nHoofdmenu\n=========")
    print("1. Inlezen en tonen CO2 data")
    print("2. Inlezen inspecteursbestanden")
    print("3. Overzicht inspecteurs")
    print("4. Inlezen bedrijfsbestanden")  # Inlezen Bedrijven (bedrijven.txt)
    print("5. Overzicht bedrijvenrapporten")
    print("6. Inlezen bezoeksrapporten")  # Inlezen Bezoeken (bezoekrapporten.txt)
    print("7. Overzicht bezoeksrapporten")
    print("8. Bereken uitstoot en boete per bedrijf")
    print(
        "9. Analyse rapport"
    )  # laat een rapportage zien van plekken met hoge waardes gas waar onbekende bedrijven zitten
    print("0. stoppen\n")

    try:
        keuze = int(input("Uw keuze : "))
    except ValueError:
        keuze = -1

    if keuze == 1:
        # mm.lees_gas_co2()
        print("implement something...")
    elif keuze == 2:
        mi.lees_inspecteurs()
    elif keuze == 3:
        mi.toon_inspecteurs()
    elif keuze == 4:
        bedrijven.lees_bedrijven()
    elif keuze == 5:
        bedrijven.toon_bedrijven()
    elif keuze == 6:
        rapporten.lees_rapporten()
    elif keuze == 7:
        handle_bezoeksrapport_keuze()
    elif keuze == 8:
        bedrijven.bereken_bedrijven_uitstoot()
        bedrijven.bereken_bedrijven_boete()
    elif keuze == 9:
        try:
            extra_waarde = int(input("Geef een waarde tussen 1 en 20: "))
            if 1 <= extra_waarde <= 20:
                mm.analyse_rapport_berekenen(extra_waarde)
            else:
                print("Ongeldige waarde. De waarde moet tussen 1 en 20 liggen.")
        except ValueError:
            print("Ongeldige invoer. Probeer opnieuw.")
    elif keuze == 0:
        break
    else:
        print("ongeldige keuze")
