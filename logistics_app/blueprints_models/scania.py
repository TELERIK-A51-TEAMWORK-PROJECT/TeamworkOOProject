from blueprints_models.company_trucks import CompanyTrucks
from blueprints_models.truck_models import Truck_Models


class Scania(CompanyTrucks):
    def __init__(self, vehicle_id: int, model_name: str, capacity_kg: int, max_range: int):
        super().__init__(vehicle_id, model_name, capacity_kg, max_range)
        self.number_of_vehicles = 10
        self.model_name = model_name
    
    @property
    def model_name(self):
        return self._model_name
    
    @model_name.setter
    def model_name(self, value):

        if value != Truck_Models.SCANIA:
            raise ValueError(f'Invalid name: {value}')
        self._model_name = value
    
    @property
    def max_range(self):
        return self._max_range
    
    @max_range.setter
    def max_range(self,value):
        if value < 0 or value > 8000:
            raise ValueError(f'Invalid range for truck with model Scania')
        self._max_range = value

    @property
    def vehicle_id(self):
        return self._vehicle_id
    
    @vehicle_id.setter
    def vehicle_id(self,value):
        if value < 1001 or value > 1010:
            raise ValueError(f'Invalid id for truck with model Scania')
        self._vehicle_id = value