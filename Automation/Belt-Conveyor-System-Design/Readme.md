# Belt Conveyor System Design

This project presents the engineering design of a 20-meter inclined belt conveyor for bulk material handling. The system is intended to transport bagged material upward at a 7° incline, with a throughput requirement of **720 tons per hour**.

The goal of this document is to demonstrate mechanical calculation methodology, power sizing, component selection, and industrial automation criteria.

---

## System Overview

| Parameter | Value |
|----------|-------|
| Conveyor length | 20 m |
| Inclination | 7° |
| Belt width | 30 in |
| Load capacity | 50 kg per meter |
| Required throughput | 720 ton/h |
| Pulley diameter (drive) | 24 in |
| Motor nominal speed | 1760 rpm |

The conveyor is designed to operate with continuous duty and stable load distribution.

---

## Mechanical Design Variables

- **Tx** – Tension to move the empty belt  
- **Ty** – Tension to move the horizontal load  
- **Tz** – Tension required to lift the material  
- **Te** – Effective tension (system total)
- **Fx** – Friction factor for an empty belt (typically 0.035)  
- **Fy** – Friction factor for loaded belt (from table: 0.04)  
- **L** – Conveyor length [ft]  
- **H** – Vertical lift [ft]  
- **S** – Belt speed [ft/min]  
- **Q** – Load weight per unit length [lb/ft]  
- **G** – Belt weight per unit length [lb/ft]  

The design follows standard belt conveyor sizing practices used in industrial material-handling systems.

---

## Tension Calculations

The following tensions were obtained based on conveyor length, load, incline, and friction coefficients:

- **Tx** – Empty belt tension  
- **Ty** – Horizontal load tension  
- **Tz** – Vertical lift tension  
- **Te** – Effective operating tension  
- **T1 / T2** – Tight-side and slack-side tension  
- **K = 0.38** – Transmission factor  
- **Tu** – Unit operating tension  

These values determine the required torque at the drive pulley and the power rating of the motor.

---

## Power and Torque Requirements

- **HPm** – Power required at the drive pulley  
- **HP** – Motor rated horsepower  
- **Reduction ratio** – 15.5:1 (selected)  
- Torque is calculated based on pulley diameter, system tension, and reduction ratio.

---

## Component Selection
### Motor

A 20 HP three-phase induction motor was selected based on the effective tension, required torque at the drive pulley, and the operating duty of the conveyor. The selected model provides sufficient starting torque, adequate overload capability, and maintains efficiency under continuous material-handling load.

**Selected Model:** Siemens 1LE0141-1DB46-4AA4  
**Frame size:** 160L  
**Rated power:** 15 kW (20 HP)  
**Rated speed:** 1760 rpm  
**Nominal torque:** 81.4 Nm  
**Efficiency:** 91.0 %  
**Power factor:** 0.84  
**Nominal current:**  
- 220 V → 51 A  
- 380 V → 29.5 A  
- 440 V → 25.5 A  
**Starting characteristics:**  
- Starting current: 8 × In  
- Starting torque: 2.2 × Tn  
- Maximum torque: 3.5 × Tn  
**Weight:** 110 kg  

This motor provides the torque margin required for inclined conveyor startup, even under partial loading, while maintaining stable thermal performance for continuous-duty operation.


### **Gearbox**
Cleveland 80AF Right Angle Dual Output Shaft (Model #44152)

### **Electrical Protections**
- **MCCB / Breaker:** 3VA5215-5EC31-0AA0  
- **Contactor:** 3RT2027-1AU20  
- **Thermal Overload Relay:** 3RU2136-4FB0  
- **Pushbutton Station:** AC 380 V / 5 A

These devices ensure safe operation, overload protection, and standardized motor-control wiring.
<img width="1281" height="711" alt="image" src="https://github.com/user-attachments/assets/ab8828b5-29d9-4c2b-9036-190dd7b350be" />


