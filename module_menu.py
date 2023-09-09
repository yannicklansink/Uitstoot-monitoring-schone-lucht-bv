# module_menu.py

import module_inspecteurs as mi
import module_metingen    as mm


#start applicatie
 
while True :
    print('\nHoofdmenu\n=========')
    print('1. Inlezen inspecteursbestand')
    print('2. Inlezen en tonen CO2 data')
    print('3. Overzicht inspecteurs')
    print('4. <invullen>')
    print('5. <invullen>')
    print('6. <invullen>')
    print('7. <invullen>')
    print('0. stoppen\n')

    try :
        keuze = int(input('Uw keuze : '))
    except ValueError :
        keuze = -1

    if keuze == 1 :
        mi.lees_inspecteurs()
    elif keuze == 2 :
        mm.lees_gas_co2()
    elif keuze == 3 :
        mi.toon_inspecteurs()
    elif keuze == 4 :
        pass
    elif keuze == 5 :
        pass
    elif keuze == 6 :
        pass
    elif keuze == 7 :
        pass
    elif keuze == 0 :
        break
    else :
        print('ongeldige keuze')