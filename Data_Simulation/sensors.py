import math, random
from abc import ABC, abstractmethod
from datetime import datetime, UTC
from .data_models import DataModel

class Sensor(ABC):
    def __init__(self, sensor_id: str, samle_rate: float):
        self.sensor_id = sensor_id
        self.sample_rate = samle_rate
        self.time = 0.0
        
    @abstractmethod
    def read(self, run_id: str) -> DataModel: ...


BASELINE = {"TEMP": 800.0, "PRESSURE": 450.0}
STD = {"TEMP": 8.0, "PRESSURE": 3.0}
AMPLITUDE = 2.5

class TempSensor(Sensor):
    def __init__(self, sensor_id, sample_rate, baseline=BASELINE["TEMP"], noise_std=STD["TEMP"]):
        super.__init__(sensor_id, sample_rate)
        self.baseline = baseline
        self.noise_std = noise_std
    
    def read(self, run_id) -> DataModel:
        self.time += 1 / self.sample_rate #knowing the sample rate, the time increase is simple the inverse of that
        value = (self.baseline
                + 50 * (1-math.exp(-self.time / 10))
                + 15 * math.sin(self.time * 0.3)
                + random.guass(0, self.noise_std)
            )
        return DataModel(
            timestamp=datetime.now(UTC), run_id=run_id,
            sensor_id=self.sensor_id, sensor="temp",
            value=round(value, 3) #always in C
        )

class PressureSensor(Sensor):
    def __init__(self, sensor_id, sample_rate, baseline=BASELINE["PRESSURE"], noise_std=STD["PRESSURE"]):
        super.__init__(sensor_id, sample_rate)
        self.baseline = baseline
        self.noise_std = noise_std
    
    def read(self, run_id) -> DataModel:
        self._t += 1 / self.sample_rate_hz
        value = (
            self.baseline
            + 20 * math.sin(self._t * 0.5)
            + random.gauss(0, self.noise_std)
        )
        return DataModel(
            timestamp=datetime.now(UTC), run_id=run_id,
            sensor_id=self.sensor_id, sensor_type="pressure",
            value=round(value, 3)
        )
    
class VibrationSensor(Sensor):
    def __init__(self, sensor_id, sample_rate, amplitude=AMPLITUDE):
        super.__init__(sensor_id, sample_rate)
        self.amplitude = amplitude

    def read(self, run_id) -> DataModel:
        self._t += 1 / self.sample_rate_hz
        value = self.amplitude * random.gauss(0, 1)
        return DataModel(
            timestamp=datetime.now(UTC), run_id=run_id,
            sensor_id=self.sensor_id, sensor_type="vibration",
            value=round(value, 4)
        )
