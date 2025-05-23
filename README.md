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

## Repository Structure

