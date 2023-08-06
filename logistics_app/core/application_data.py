from blueprints_models.company_trucks import CompanyTrucks
from blueprints_models.actros import Actros
from blueprints_models.scania import Scania
from blueprints_models.man import Man

class ApplicationData:
    def __init__(self):
        self._vehicles = []

    @property
    def vehicles(self):
        return tuple(self._vehicles)
    
    def find_vehicle_by_name(self,name) -> CompanyTrucks:
        for vehicle in self._vehicles:
            if vehicle.name == name:
                return vehicle
        else:
            raise ValueError(f'Vehicle with this {name} does not exist!')
        
    def create_scania(self,vehicle_id,name,capacity,max_range):
        scania = Scania(vehicle_id,name,capacity,max_range)
        self._vehicles.append(scania)
        return scania
    
    def create_actros(self,vehicle_id,name,capacity,max_range):
        actros = Actros(vehicle_id,name,capacity,max_range)
        self._vehicles.append(actros)
        return actros
    
    def create_man(self,vehicle_id,name,capacity,max_range):
        man = Man(vehicle_id,name,capacity,max_range)
        self._vehicles.append(man)
        return man

    def vehicle_exists(self, name) -> bool:
        return name in [this.name for this in self._vehicles]
