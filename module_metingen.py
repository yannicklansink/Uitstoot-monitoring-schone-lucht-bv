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

    print(gasarray)
    print("------")
    print(gasarray[99])
    print(len(gasarray))
    plt.imshow(gasarray)
    plt.colorbar()
    plt.show()
