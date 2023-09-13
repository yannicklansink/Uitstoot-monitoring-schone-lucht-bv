# module_menu.py

import module_inspecteurs as mi
import module_metingen as mm
import module_bedrijven as bedrijven
import module_bezoeken as rapporten

# start applicatie

while True:
    print("\nHoofdmenu\n=========")
    print("1. Inlezen inspecteursbestand")
    print("2. Overzicht inspecteurs")
    print("3. Inlezen en tonen CO2 data")
    print("4. Inlezen Bedrijfsbestanden")  # Inlezen Bedrijven (bedrijven.txt)
    print("5. Overzicht bedrijven")
    print("6. Inlezen Bezoeksrapporten")  # Inlezen Bezoeken (bezoekrapporten.txt)
    print("7. Overzicht rapporten")
    print("0. stoppen\n")

    try:
        keuze = int(input("Uw keuze : "))
    except ValueError:
        keuze = -1

    if keuze == 1:
        mi.lees_inspecteurs()
    elif keuze == 2:
        mi.toon_inspecteurs()
    elif keuze == 3:
        mm.lees_gas_co2()
    elif keuze == 4:
        bedrijven.lees_bedrijven()
    elif keuze == 5:
        bedrijven.toon_bedrijven()
    elif keuze == 6:
        rapporten.lees_rapporten()
    elif keuze == 7:
        rapporten.toon_rapporten()
    elif keuze == 0:
        break
    else:
        print("ongeldige keuze")
