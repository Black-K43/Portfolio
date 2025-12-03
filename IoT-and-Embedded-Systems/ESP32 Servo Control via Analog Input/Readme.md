# ESP32 Servo Control with Potentiometer — 1:1 Angle Mapping

This mini-project demonstrates direct position control of a standard 180° servo using an ESP32 and a single potentiometer. The goal is to achieve a clean 1:1 mapping between the analog input (0–4095) and the servo angle (0–180°), without filtering or scaling beyond the basic conversion.

This example is part of the *Control and Embedded Systems* section of the engineering portfolio.

---

## 🎯 Objective

- Read an analog voltage using the ESP32 ADC.  
- Convert the reading to a corresponding servo angle.  
- Command the servo through PWM using the ESP32Servo library.  
- Display real-time readings via serial monitor.  

This simple setup is ideal for demonstrating fundamental motion control, ADC usage, and actuator interfacing.

---

## 🧰 Hardware

- **ESP32 Dev Board**
- **Standard hobby servo (180°)**
- **10 kΩ potentiometer**
- Jumper wires and breadboard

### Wiring
- Potentiometer center pin → GPIO 34 (ADC)
- Potentiometer outer pins → 3.3V and GND
- Servo signal → GPIO 18  
- Servo VCC → 5V external supply  
- Servo GND → Common ground with ESP32  

---
