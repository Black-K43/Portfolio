# ESP32 Casino Roulette — IPOS Position Control System

This project implements a digital roulette mechanism controlled by an ESP32 and a servo driver operating in **IPOS (Internal Position Control)** mode. The system generates a random target position and commands the driver to move the roulette wheel to one of **seven discrete positions**, each associated with a binary code sent from the ESP32.

The mechanism is designed for casino-style applications where randomness, repeatability, and fast actuation are required.

---

## 🎯 System Overview

The ESP32 generates a random number between **0 and 7**.  
This value is converted into a 3-bit binary output and sent to the driver through dedicated GPIO pins.  
Two additional digital lines (**REF** and **TRIGGER**) control the initialization sequence and movement execution:

- **REF**: Sends an initial reference pulse to synchronize the driver  
- **TRIGGER**: Tells the driver to move to the selected IPOS position  
- **BIT0, BIT1, BIT2**: Encode the target position in binary (LSB → MSB)  
- **Button Input**: Starts a new roulette cycle

The driver receives the binary position code and rotates the roulette mechanism to the corresponding internal position.

---

## ⚙️ Driver Configuration

The servo driver is configured as follows:

- **Mode:** IPOS – Internal Position Control  
- **Scaling factor:** 1:1  
- **LU value:** 36,000 (internal units per revolution)  
- **Positions:** Seven incremental positions (0–7)  
- **Speed:** Same for all positions  

These parameters ensure predictable motion and accurate positioning while maintaining randomness in selection.

---

## 🛠 Hardware Components

- ESP32 Development Board  
- Servo driver with IPOS capability  
- Servomotor mounted under the roulette table  
- Push button (start trigger)  
- Wiring for digital outputs and reference pulses  

---

## 📐 System Flow

1. System powers on  
2. ESP32 sends a **REF pulse** to the driver  
3. ESP32 generates a random number (0–7)  
4. Binary outputs (BIT0–BIT2) set the IPOS target  
5. When the button is pressed:  
   - A **TRIGGER pulse** is sent  
   - The roulette moves to the chosen position  
6. Process repeats on each press  

A flowchart illustrating this sequence is included in the `/docs/` folder.

---
<img width="1126" height="593" alt="image" src="https://github.com/user-attachments/assets/72efdae6-8f4a-4fc1-828a-598bc3af0074" />

## 🧩 MicroPython Code (ESP32)

```python
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
    print("New random number:", n)

print("Starting digital roulette system...")

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

