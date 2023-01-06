# IP Raspberry : 192.168.0.10

# Liste des 17 ports GPIOs utilisés
GPIO_LIST = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 21, 20, 16]

# on a 7 entrées et 10 sorties
# les entrées ne sont que les entrées qui acceptent le pull-down
GPIO_OUTPUT = [2, 3, 4, 5, 6, 7, 8]
GPIO_INPUT = [9, 10, 11, 12, 13, 16, 17, 18, 19, 20]



"""
Le jeu est divisé en 2 moitiés (Par l’axe qui passe entre la zone 9 et 14) l’une des 2 nappes en plastique 
contient 7 pistes conductrices: 

    une pour toutes les zones “Simple” de la moitié de la cible
    une pour toutes les zones “Simple” de l’autre moitié de la cible
    une pour toutes les zones “Double” de la moitié de la cible
    une pour toutes les zones “Double” de l’autre moitié de la cible
    une pour toutes les zones “Triple” de la moitié de la cible
    une pour toutes les zones “Triple” de l’autre moitié de la cible
    une pour le “Bull” Simple et Double

L’autre nappe contient 10 pistes, 8 des pistes correspondent chacune à une paire de zone numérotée, chacune des zones 
appartenant à une moitié différente ((9, 14) par exemple). Les 2 pistes restantes ont, en plus de la paire de zone, 
une zone du “Bull”. 
"""

PIN_TRIPLE_1 = 2  # triple deuxième moitie ok
PIN_DOUBLE_1 = 3  # double deuxième moitie ok
PIN_SINGLE_1 = 4  # simple deuxième moitie ok
PIN_BULL = 5  # bull ok
PIN_SINGLE_0 = 6  # single premiere moitie ok
PIN_DOUBLE_0 = 7  # double premiere moitie ok
PIN_TRIPLE_0 = 8  # triple premiere moitie ok

PIN_9_14_B = 9  # zone 9 et 14 ok
PIN_20_16_1 = 10  # zone 20 et 16 ok
PIN_12_11_B = 11  # zone 12 et 11 ok
PIN_5_8_2 = 12  # zone 5 et 8 ok
# PIN_6_2_3 = 13  # zone 6 et 2 ok
PIN_10_15_4 = 16  # zone 10 et 15 ok
# PIN_13_17_5 = 17  # zone 13 et 17 ok
PIN_4_3_6 = 18  # zone 4 et 3 ok
PIN_18_19_7 = 19  # zone 18 et 19 ok
PIN_1_7_8 = 20  # zone 1 et 7 ok

PIN_13_17_5 = 13  # zone 13 et 17 ok
PIN_6_2_3 = 17  # zone 6 et 2 ok
