import math, random
from abc import ABC, abstractmethod
from datetime import datetime
from .data_models import DataModel

class Sensor(ABC):
    def __init__(self, sensor_id: str, samle_rate: float):
        self.sensor_id = sensor_id
        self.sample_rate = samle_rate
        self.time = 0.0
        
    @abstractmethod
    def read(self, run_id: str) -> DataModel: ...


BASELINE = {"TEMP": 800.0, "PRESSURE": 450.0, "VIBRATION": 100}
STD = {"TEMP": 8.0, "PRESSURE": 3.0, "VIBRATION": 2.5}

class TempSensor(Sensor):
    def __init__(self, sensor_id, sample_rate, baseline=BASELINE["TEMP"], noise_std=STD["TEMP"]):
        super.__init__(sensor_id, sample_rate)
        self.baseline = baseline
        self.noise_std = noise_std
    
class PressureSensor(Sensor):
    def __init__(self, sensor_id, sample_rate, baseline=BASELINE["PRESSURE"], noise_std=STD["PRESSURE"]):
        super.__init__(sensor_id, sample_rate)
        self.baseline = baseline
        self.noise_std = noise_std
    
class VibrationSensor(Sensor):
    def __init__(self, sensor_id, sample_rate, baseline=BASELINE["VIBRATION"], noise_std=STD["VIBRATION"]):
        super.__init__(sensor_id, sample_rate)
        self.baseline = baseline
        self.noise_std = noise_std
