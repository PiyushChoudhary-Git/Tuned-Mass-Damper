# Tuned Mass Damper (TMD) – CE302 Structural Analysis Project

## Overview
This repository hosts the complete project work on the design, analysis, and testing of a **Tuned Mass Damper (TMD)** system as part of the CE302 Structural Analysis course at IIT Gandhinagar. The project investigates the performance of a TMD in mitigating structural vibrations in a model skyscraper using both analytical and experimental methods.



##  Project Components

### 1. **Theoretical Analysis**
- Derived mathematical model for TMD behaviour
- Analytical evaluation of natural frequency, deflection angle, and damping ratio
- Comparison of system response with and without TMD

### 2. **SAP2000 Modeling**
- Drafted and built a 3D skyscraper model
- Simulated earthquake loads
- Analyzed energy dissipation characteristics

### 3. **Physical Experimentation**
- Constructed a scaled MDF-based model
- Used MPU6050 accelerometer with Arduino Uno
- Recorded real-time acceleration data
- Computed damping ratios using logarithmic decrement

### 4. **Data Analysis (Python)**
- Real-time data plotting and CSV storage
- Peak detection for damping analysis
- Graphical comparison of system responses

---

## Key Results
| Parameter        | Without TMD | With TMD |
|------------------|-------------|----------|
| Natural Frequency| ~2.88 Hz    | ~2.50 Hz |
| Damping Ratio    | 1.95%       | 3.77%    |
| Stabilization Time (Sim.) | >3.0 sec | 2.6 sec |


---

## 🔧 Tools & Technologies
- **SAP2000** for structural simulation
- **Arduino IDE** for sensor interfacing
- **Python (Matplotlib, SciPy, Pandas)** for data processing
- **MPU6050** IMU sensor for acceleration tracking

---

## 🎓 Acknowledgements
Special thanks to:
- **Prof. Manish Kumar** (Course Instructor)
- Teaching Assistants – **Krishnaveni Ma’am** and **Priya Ben Ma’am**

---

## 📜 License
This project is for academic purposes under the Structural Analysis course (CE302). You are welcome to use it however you may like.

---

## 📎 References
1. [Purdue University - Intro to Structural Motion Control](https://engineering.purdue.edu/~ce573/Documents/Intro%20to%20Structural%20Motion%20Control_Chapter4.pdf)
2. [GY-91 MPU9250 Wiring Guide – Electropeak](https://electropeak.com/learn/wp-content/uploads/2020/11/GY91-IMU-wire.jpg)

