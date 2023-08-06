from blueprints_models.truck_models import Truck_Models

class CompanyTrucks:
    def __init__(self, vehicle_id: int, model_name: str, capacity_kg: int, max_range: int):
        self.vehicle_id = vehicle_id
        self._model_name = model_name
        self.capacity_kg = capacity_kg
        self.max_range = max_range
        self.number_of_vehicles = 0

    # Id checker
    @property
    def vehicle_id(self):
        return self._vehicle_id
    
    @vehicle_id.setter
    def vehicle_id(self,value):
        if value < 1001 or value > 1040:
            raise ValueError('The id you are trying to input is invalid(too low or too high)')
        self._vehicle_id = value

    # Model name checker
    @property
    def model_name(self):
        return Truck_Models.from_string(self._model_name)
    
    #Capacity checker
    @property
    def capacity_kg(self):
        return self._capacity_kg
    
    @capacity_kg.setter
    def capacity_kg(self,value):
        if value < 0 or value > 42000:
            raise ValueError('The capacity you are trying to input is invalid (too low or too high)')
        self._capacity_kg = value

    #Max range checker
    @property
    def max_range(self):
        return self._max_range
    
    @max_range.setter
    def max_range(self,value):
        if value < 0 or value > 13000:
            raise ValueError('This vehicle you are trying to input is invalid (too low or too high)')
        self._max_range = value