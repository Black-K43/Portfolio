<img width="1081" height="713" alt="image" src="https://github.com/user-attachments/assets/ff72373b-042d-478f-95f1-7bedf257e61d" />
# Induction Motor Simulation — MATLAB/Simulink

This project presents the simulation of a three-phase squirrel-cage induction motor using MATLAB and Simulink.  
The objective is to analyze the motor’s dynamic behavior under load and to extract core electromechanical variables such as **torque**, **rotor speed**, **stator current**, and **phase voltage**.

The simulation is intended as a compact demonstration of control and motor-modeling skills for an engineering portfolio.

---

## 🎯 Objective

To model and simulate the transient and steady-state behavior of a three-phase induction motor, and evaluate its dynamic response in terms of:

- Electromagnetic torque  
- Rotor angular velocity  
- Stator phase current  
- Stator line voltage  

---

## 🧩 System Description

The model is based on the standard **dq0 reference frame** representation of induction machines.  
MATLAB/Simulink provides the “Asynchronous Machine” block, which is configured with the mechanical and electrical parameters of the motor.

The simulation includes:

- Three-phase power supply  
- Asynchronous machine (squirrel-cage type)  
- Mechanical load  
- Measurement blocks  
- Scope and logging outputs  

---

## 🧮 Motor Model Equations (Simplified)

The analytical foundation is given by the classical induction motor equations:

### 1. Electromagnetic Torque  
\[
T_e = \frac{3}{2} p \, (\psi_d i_q - \psi_q i_d)
\]

### 2. Stator Voltage Equations  
\[
v_d = R_s i_d + \frac{d\psi_d}{dt} - \omega_e \psi_q
\]  
\[
v_q = R_s i_q + \frac{d\psi_q}{dt} + \omega_e \psi_d
\]

### 3. Rotor Flux Linkage  
\[
\psi_d = L_s i_d + L_m i_{dr}
\]  
\[
\psi_q = L_s i_q + L_m i_{qr}
\]

### 4. Mechanical Dynamics  
\[
J \frac{d\omega_m}{dt} = T_e - T_L - B\omega_m
\]

These equations describe how torque, electrical currents and rotor speed evolve during the simulation.

A full explanation is available in `/docs/motor_equations.md`.

---

## 🧪 Simulation Results

The following variables were extracted from the Simulink model:

- **Electromagnetic torque (N·m)**  
- **Rotor speed (rpm)**  
- **Stator phase current (A)**  
- **Stator line voltage (V)**  


