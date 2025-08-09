# This is a Medical Device Simulator for a Temperature Sensor

A cross-language demonstration of **Object-Oriented Programming** and **applications/embedded software development** using **Python** 

This project simulates a set of temperature sensors, logs their readings, and raises alerts if a threshold is exceeded. The architecture is implemented in Python 

---

## Features
- OOP design: base `Sensor` class + derived `TemperatureSensor`
- Threshold-based alert system
- Maintains a rolling log of the last 10 readings
- Simulates embedded system behavior
- Implemented in Python 

---

## 1. Python Version

**Run:**
```bash
cd python
python sensor_sim.py
```

**Example Output:**
```
ALERT: Sensor T1 exceeded threshold! Value: 39.42C
Sensor T1 Log: [37.82, 39.42, 36.15, ...]
```







