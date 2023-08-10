from blueprints_models.company_trucks import CompanyTrucks


class Man(CompanyTrucks):
    def __init__(self, vehicle_id: int,capacity_kg: int, max_range: int):
        super().__init__(vehicle_id,capacity_kg, max_range)
    
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
        if value < 10000 or value > 10000:
            raise ValueError(f'Invalid range for truck with model Man')
        self._max_range = value

    @property
    def vehicle_id(self):
        return self._vehicle_id
    
    @vehicle_id.setter
    def vehicle_id(self,value):
        if value < 1011 or value > 1025:
            raise ValueError(f'Invalid id for truck with model Man')
        self._vehicle_id = value