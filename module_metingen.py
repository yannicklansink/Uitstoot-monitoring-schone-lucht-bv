# module_metingen.py

import numpy             as np
import matplotlib.pyplot as plt

#constanten
GASSENBESTAND = 'c:\\pyopdracht\\gassen.csv'


def lees_gas_co2() :
    """Inlezen CO2 data vanuit het csv-gassenbestand en plotten data"""
    gasarray = (np.loadtxt(GASSENBESTAND, delimiter=',', skiprows=1, usecols=2)).reshape(100,100)

    print(gasarray)
    plt.imshow(gasarray)
    plt.colorbar()
    plt.show()

