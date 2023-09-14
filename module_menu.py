# module_menu.py

import module_inspecteurs as mi
import module_metingen as mm
import module_bedrijven as bedrijven
import module_bezoeken as rapporten

# start applicatie

while True:
    print("\nHoofdmenu\n=========")
    print("1. Inlezen en tonen CO2 data")
    print("2. Inlezen inspecteursbestand")
    print("3. Overzicht inspecteurs")
    print("4. Inlezen bedrijfsbestanden")  # Inlezen Bedrijven (bedrijven.txt)
    print("5. Overzicht bedrijvenrapporten")
    print("6. Inlezen bezoeksrapporten")  # Inlezen Bezoeken (bezoekrapporten.txt)
    print("7. Overzicht bezoeksrapporten")
    print("8. Plot bedrijven uitstoot")  # work in progress
    print("0. stoppen\n")

    try:
        keuze = int(input("Uw keuze : "))
    except ValueError:
        keuze = -1

    if keuze == 1:
        mm.lees_gas_co2()
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
        rapporten.toon_rapporten()
    elif keuze == 8:
        bedrijven.bereken_bedrijven_uitstoot()
    elif keuze == 0:
        break
    else:
        print("ongeldige keuze")
