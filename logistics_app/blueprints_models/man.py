from blueprints_models.company_trucks import CompanyTrucks
from blueprints_models.truck_models import Truck_Models



class Man(CompanyTrucks):
    def __init__(self, vehicle_id: int, model_name: str, capacity_kg: int, max_range: int):
        super().__init__(vehicle_id, model_name, capacity_kg, max_range)
        self.model_name = model_name

    @property
    def model_name(self):
        return self._model_name
    
    @model_name.setter
    def model_name(self, value):

        if value != Truck_Models.MAN:
            raise ValueError(f'Invalid name: {value}')
        self._model_name = value
    
    @property
    def capacity_kg(self):
        return self._capacity_kg
    
    @capacity_kg.setter
    def capacity_kg(self,value):
        if value < 0 or value > 37000:
            raise ValueError(f'Invalid capacity for truck with model Man')
        self._capacity_kg = value

    @property
    def max_range(self):
        return self._max_range
    
    @max_range.setter
    def max_range(self,value):
        if value < 0 or value > 10000:
            raise ValueError(f'Invalid range for truck with model Man')
        self._max_range = value

    @property
    def vehicle_id(self):
        return self._vehicle_id
    
    @vehicle_id.setter
    def vehicle_id(self,value):
        if value < 1011 or value > 1025:
            raise ValueError(f'Invalid id for truck with model {self._model_name}')
        self._vehicle_id = value