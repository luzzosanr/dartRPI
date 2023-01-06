from Configuration import GPIO_INPUT, GPIO_OUTPUT


def setup_gpio(GPIO):
    """
    Initialise les ports GPIOs
    """
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for gpio in GPIO_INPUT:  # On met tous les ports GPIOs en entrée
        GPIO.setup(gpio, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for gpio in GPIO_OUTPUT:  # On met tous les ports GPIOs en sortie
        GPIO.setup(gpio, GPIO.OUT)
        GPIO.output(gpio,1)


def read_gpio(GPIO):
    """
    Lit les ports GPIOs et renvoie tous les GPIOs qui sont à 1
    """
    gpio_on = []
    for port in GPIO_LIST:
        if GPIO.input(port) == 1:
            gpio_on.append(port)
    return gpio_on







