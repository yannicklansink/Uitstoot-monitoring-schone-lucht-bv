import os
import numpy as np
import matplotlib.pyplot as plt

# Constants
CURRENT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
GASSENBESTAND = os.path.join(CURRENT_DIRECTORY, "sample-files", "gassen.csv")


def lees_gas_co2():
    """Inlezen CO2 data vanuit het csv-gassenbestand en plotten data"""
    gasarray = (
        np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=2)
    ).reshape(100, 100)

    plt.imshow(gasarray)
    plt.colorbar()
    plt.show()


# Load all gas data into arrays
co2_data = np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=2).reshape(100, 100)
ch4_data = np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=3).reshape(100, 100)
no2_data = np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=4).reshape(100, 100)
nh3_data = np.loadtxt(GASSENBESTAND, delimiter=",", skiprows=1, usecols=5).reshape(100, 100)


def getUitstootGasCO2(breedtegraad, lengtegraad):
    return co2_data[int(breedtegraad), int(lengtegraad)]

def getUitstootGasCH4(breedtegraad, lengtegraad):
    return ch4_data[int(breedtegraad), int(lengtegraad)]

def getUitstootGasNO2(breedtegraad, lengtegraad):
    return no2_data[int(breedtegraad), int(lengtegraad)]

def getUitstootNH3(breedtegraad, lengtegraad):
    return nh3_data[int(breedtegraad), int(lengtegraad)]
