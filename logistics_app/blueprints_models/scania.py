from blueprints_models.company_trucks import CompanyTrucks


class Scania(CompanyTrucks):
    def __init__(self, vehicle_id: int, capacity_kg: int, max_range: int):
        super().__init__(vehicle_id, capacity_kg, max_range)
        self.scanias = []
    
    @property
    def max_range(self):
        return self._max_range
    
    @max_range.setter
    def max_range(self,value):
        if value < 8000 or value > 8000:
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