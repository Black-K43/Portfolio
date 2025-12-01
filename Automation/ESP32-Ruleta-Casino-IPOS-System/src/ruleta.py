from machine import Pin
import time
import random

# Control pins
REF = Pin(2, Pin.OUT)
TRIGGER = Pin(4, Pin.OUT)

# Binary output pins (LSB → MSB)
BIT0 = Pin(18, Pin.OUT)
BIT1 = Pin(19, Pin.OUT)
BIT2 = Pin(21, Pin.OUT)

# Push button (active low)
BOTON = Pin(15, Pin.IN, Pin.PULL_UP)

def pulso(pin, duracion_ms=100):
    """Generate a short pulse on the given pin."""
    pin.value(1)
    time.sleep_ms(duracion_ms)
    pin.value(0)

def mostrar_numero_en_bits(n):
    """Output a 3-bit number to BIT0, BIT1, BIT2."""
    BIT0.value(n & 0b001)
    BIT1.value((n >> 1) & 0b001)
    BIT2.value((n >> 2) & 0b001)

def generar_y_mostrar_aleatorio():
    """Generate a random number between 0 and 7 and display it."""
    n = random.randint(0, 7)
    mostrar_numero_en_bits(n)
    print("Nuevo número aleatorio:", n)

print("Iniciando sistema de ruleta digital...")

# Initial REF pulse
pulso(REF, 100)
generar_y_mostrar_aleatorio()

ultimo_estado = BOTON.value()

while True:
    estado = BOTON.value()

    # Detect falling edge → button pressed
    if estado == 0 and ultimo_estado == 1:
        pulso(TRIGGER, 100)        # Movement command
        generar_y_mostrar_aleatorio()
        time.sleep_ms(200)

    ultimo_estado = estado

