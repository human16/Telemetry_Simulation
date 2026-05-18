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

class TempSensor(Sensor):
    def __init__(self, sensor_id, sample_rate, baseline=800.0, noise_std=5.0):
        pass
