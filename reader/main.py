"""
On a 17 broches GPIOs. Donc 7 entrées et 10 sorties.
On va envoyer un signal sur chaque sortie périodiquement et rapidement.
On a des interruptions sur les entrées.
"""

import RPi.GPIO as GPIO
import time

from Configuration import *
from functions import setup_gpio

import requests

activated_out_pin = 0
une_fois_sur_deux = False
not_detected = True
last_in_pins = []
last_out_pin = 0


def touch(gpio_in, gpio_out):
    """
    Fonction qui est appelée quand une touche sur la cible est détectée.
    :param gpio_in:
    :param gpio_out:
    :return:
    """

    output_dictionary = {}
    output_dictionary[PIN_TRIPLE_1] = [3, 0]  # triple deuxième moitie
    output_dictionary[PIN_DOUBLE_1] = [2, 0]  # double deuxième moitie
    output_dictionary[PIN_SINGLE_1] = [1, 0]  # simple deuxième moitie
    output_dictionary[PIN_BULL] = [0, 2]      # bull
    output_dictionary[PIN_SINGLE_0] = [3, 1]  # single premiere moitie
    output_dictionary[PIN_DOUBLE_0] = [1, 1]  # double premiere moitie
    output_dictionary[PIN_TRIPLE_0] = [2, 1]  # triple premiere moitie

    input_dictionary = {}
    input_dictionary[PIN_9_14_B] = [9, 14, 50] # zone 9 ou zone 14 ou bull
    input_dictionary[PIN_20_16_1] = [20, 16, 1]
    input_dictionary[PIN_12_11_B] = [12, 11, 25]
    input_dictionary[PIN_5_8_2] = [5, 8, 2]
    input_dictionary[PIN_6_2_3] = [6, 2, 3]
    input_dictionary[PIN_10_15_4] = [10, 15, 4]
    input_dictionary[PIN_13_17_5] = [13, 17, 5]
    input_dictionary[PIN_4_3_6] = [4, 3, 6]
    input_dictionary[PIN_18_19_7] = [18, 19, 7]
    input_dictionary[PIN_1_7_8] = [1, 7, 8]

    # output_dictionary[gpio_out][1]  # 0 (premiere moitie) ou 1 (seconde moitie) ou 2 (bull)
    # input_dictionary[gpio_in]  # par exemple [9, 14, 50]
    value = input_dictionary[gpio_in][output_dictionary[gpio_out][1]]
    multiple = output_dictionary[gpio_out][0]
    if multiple == 0:
        multiple = 1
        if value == 50:
            multiple = 2
            value = 25
        elif value == 25:
            multiple = 1

    print("onDartTargetTouch: ", multiple, value)
    requests.get(f"http://192.168.43.113/add_shot/?gpio={multiple}{value}")
    time.sleep(0.8)


def generate_signals():
    # envoie un signal sur chaque sortie
    for gpio_out in GPIO_OUTPUT:
        GPIO.output(gpio_out, 1)
        # time.sleep(0.1)
        for gpio_in in GPIO_INPUT:
            if GPIO.input(gpio_in) == 1:
                print("touché ! \t gpio_in: \t", gpio_in, "gpio_out: \t", gpio_out)
                touch(gpio_in, gpio_out)
            # time.sleep(0.01)

        GPIO.output(gpio_out, 0)


# Dictionnaire qui associe les ports GPIOs aux codes
gpio_mapping = {}

setup_gpio(GPIO)

# on définit des interruptions sur toutes les entrées
# for gpio in GPIO_INPUT:
#     GPIO.add_event_detect(gpio, GPIO.FALLING, callback=callback)

while True:
    # print a colored line
    # print("\033[1;32;40m" + "\n--------waiting for a signal--------" + "\033[0;37;40m")
    generate_signals()
