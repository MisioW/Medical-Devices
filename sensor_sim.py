import random
import time

class Sensor:
    def __init__(self, sensor_id, threshold):
        self.sensor_id = sensor_id
        self.threshold = threshold
        self.readings = []

    def log_reading(self, value):
        self.readings.append(value)
        if len(self.readings) > 10:
            self.readings.pop(0)

    def get_log(self):
        return self.readings


class TemperatureSensor(Sensor):
    def read_temperature(self):
        return round(random.uniform(35.0, 40.0), 2)

    def check_threshold(self, value):
        if value > self.threshold:
            print(f"ALERT: Sensor {self.sensor_id} exceeded threshold! Value: {value}C")


if __name__ == "__main__":
    sensor1 = TemperatureSensor("T1", 38.5)

    for _ in range(15):
        temp = sensor1.read_temperature()
        sensor1.log_reading(temp)
        sensor1.check_threshold(temp)
        print(f"Sensor {sensor1.sensor_id} Log: {sensor1.get_log()}")
        time.sleep(0.2)
