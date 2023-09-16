import os
import numpy as np
import matplotlib.pyplot as plt
import module_bedrijven as bedrijven

# Constants
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
GASSENBESTAND = os.path.join(CURRENT_DIRECTORY, "sample-files", "gassen.csv")


# def lees_gas_co2():
#     """Inlezen CO2 data vanuit het csv-gassenbestand en plotten data"""
#     gasarray = (
#         np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=2)
#     ).reshape(100, 100)

#     plt.imshow(gasarray)
#     plt.colorbar()
#     plt.show()


# Load all gas data into arrays
co2_data = np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=2).reshape(
    100, 100
)
ch4_data = np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=3).reshape(
    100, 100
)
no2_data = np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=4).reshape(
    100, 100
)
nh3_data = np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=5).reshape(
    100, 100
)

bekende_bedrijven_locaties = np.zeros([100, 100])


def analyse_rapport_berekenen(number_of_locaties):
    """opsporen van vervuilende plekken waar onbekende bedrijven gevestigt zijn"""
    if not np.any(bekende_bedrijven_locaties):
        print(
            "Geen bekende bedrijfslocaties gevonden.\nBereken eerst de uitstoot en boete per bedrijf.\nDe analyse wordt gestopt."
        )
        return

    # Alle waarden in de array waar bedrijven zitten op 0 zetten
    totale_gasses = np.empty_like(co2_data)

    for i in range(0, 100):
        for j in range(0, 100):
            if bekende_bedrijven_locaties[i, j] >= 1:
                # Bedrijven gevestigt op deze plek
                totale_gasses[i, j] = 0
                continue
            totale_gasses[i, j] = (
                bedrijven.C1 * co2_data[i][j]
                + bedrijven.C2 * ch4_data[i][j]
                + bedrijven.C3 * no2_data[i][j]
                + bedrijven.C4 * nh3_data[i][j]
            )
    lijst_vervuilende_plekken = get_lijst_met_meest_vervuilende_locaties(
        totale_gasses, number_of_locaties
    )
    # Het metingenbestand bevat minimaal 1 zo’n locatie en de functie
    # moet de coördinaten van deze locatie en de gemeten concentraties tonen.
    # In het analyserapport moet functioneel beschreven worden hoe het programma deze analyse uitvoert
    print_analyse_rapport_met_gas_waarden(lijst_vervuilende_plekken)


def get_lijst_met_meest_vervuilende_locaties(array_to_check, number_of_locaties):
    """returns een lijst met tuples met de locaties van de hoogst gemeten waarden en waarden zelf"""
    gesorteerde_indexen = np.argsort(array_to_check.ravel())

    hoogste_locatie_indexen = gesorteerde_indexen[-number_of_locaties:][::-1]

    hoogste_locatie_2D_indexen = np.unravel_index(
        hoogste_locatie_indexen, array_to_check.shape
    )

    locaties = [
        (i, j, format(array_to_check[i, j], ".2f"))
        for i, j in zip(hoogste_locatie_2D_indexen[0], hoogste_locatie_2D_indexen[1])
    ]
    return locaties


def print_analyse_rapport_met_gas_waarden(locaties):
    print("=" * 60)
    print(" " * 15 + "Analyse Rapport Gas Waarden")
    print("=" * 60)

    if not locaties:
        print("\nGeen locaties gevonden met hoog gemeten gas waarden.")
        return

    if len(locaties) == 1:
        print("\nEr is 1 locatie gevonden met een hoog gemeten gas waarde:")
    else:
        print(
            f"\nEr zijn {len(locaties)} locaties gevonden met hoog gemeten gas waarden:"
        )

    print("\nLocatie (x, y)  |  Totale Gas Waarde")
    print("-" * 35)

    for locatie in locaties:
        try:
            totale_gas_waarde = float(locatie[2])
        except ValueError:
            totale_gas_waarde = locatie[2]

        print(
            f"  ({locatie[0]:>2}, {locatie[1]:<2})     |       {totale_gas_waarde:.2f}"
        )
    print("=" * 60)
    print("\nFunctionele Beschrijving van de Analyse")
    print("-" * 40)
    print(
        "Het programma verzamelt informatie over de bekende bedrijfslocaties en de gemeten gaswaarden zoals CO2, CH4, NO2 en NH3.."
    )
    print(
        "Het negeert de gebieden waar bekende bedrijven zijn gevestigd om te focussen op het identificeren van mogelijke onbekende vervuilers."
    )
    print(
        "Het berekent de totale uitstoot voor elke locatie op basis van de gemeten waarden van verschillende gassen."
    )
    print(
        "Het identificeert de locaties met de hoogste uitstootwaarden die niet geassocieerd zijn met bekende bedrijven."
    )
    print(
        "Deze locaties zijn hierboven gerapporteerd als de meest vervuilende plekken, zodat ze verder kunnen worden onderzocht."
    )
    print("=" * 60)


def get_uitstoot_gas_CO2(breedtegraad, lengtegraad):
    bekende_bedrijven_locaties[breedtegraad, lengtegraad] = 1
    return co2_data[int(breedtegraad), int(lengtegraad)]


def get_uitstoot_gas_CH4(breedtegraad, lengtegraad):
    bekende_bedrijven_locaties[breedtegraad, lengtegraad] = 1
    return ch4_data[int(breedtegraad), int(lengtegraad)]


def get_uitstoot_gas_NO2(breedtegraad, lengtegraad):
    bekende_bedrijven_locaties[breedtegraad, lengtegraad] = 1
    return no2_data[int(breedtegraad), int(lengtegraad)]


def get_uitstoot_NH3(breedtegraad, lengtegraad):
    bekende_bedrijven_locaties[breedtegraad, lengtegraad] = 1
    return nh3_data[int(breedtegraad), int(lengtegraad)]
