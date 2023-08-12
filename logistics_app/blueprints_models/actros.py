
class Actros():
    def __init__(self, vehicle_id: int,capacity_kg: int, max_range: int):
        self.vehicle_id = vehicle_id
        self.capacity_kg = capacity_kg
        self.max_range = max_range

    @property
    def capacity_kg(self):
        return self._capacity_kg
    
    @capacity_kg.setter
    def capacity_kg(self,value):
        if value < 0 or value > 26000:
            raise ValueError(f'Invalid capacity for truck with model Actros')
        self._capacity_kg = value

    @property
    def max_range(self):
        return self._max_range
    
    @max_range.setter
    def max_range(self,value):
        if value < 13000 or value > 13000:
            raise ValueError(f'Invalid range for truck with model Actros')
        self._max_range = value
