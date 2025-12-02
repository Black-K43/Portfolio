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

## Motor Model Equations (Simplified)

The induction motor model is described using the classical dq0 representation.  
Below are clean, simplified engineering equations suitable for documentation.

**1. Electromagnetic Torque**
Te = (3/2) * p * (psi_d * i_q – psi_q * i_d)

**2. Stator Voltage Equations**
v_d = Rs * i_d + d(psi_d)/dt – we * psi_q  
v_q = Rs * i_q + d(psi_q)/dt + we * psi_d

**3. Flux Linkage Relations**
psi_d = Ls * i_d + Lm * i_dr  
psi_q = Ls * i_q + Lm * i_qr

**4. Mechanical Dynamics**
J * d(wm)/dt = Te – TL – B * wm


---

## 🧪 Simulation Results

The following variables were extracted from the Simulink model:

- **Electromagnetic torque (N·m)**  
- **Rotor speed (rpm)**  
- **Stator phase current (A)**  
- **Stator line voltage (V)**  


