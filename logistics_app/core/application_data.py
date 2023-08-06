from blueprints_models.company_trucks import CompanyTrucks
from blueprints_models.actros import Actros
from blueprints_models.scania import Scania
from blueprints_models.man import Man
from logistics_info.route import RouteOfTrucks

class ApplicationData:
    SCANIA_NUMBER_OF_TRUCKS = 10
    MAN_NUMBER_OF_TRUCKS = 15
    ACTROS_NUMBER_OF_TRUCKS = 15
    def __init__(self):
        self._trucks = []

    @property
    def trucks(self):
        return tuple(self._trucks)
    
    def find_truck_by_id(self, id) -> CompanyTrucks:
        for truck in self._trucks:
            if truck.vehicle_id == id:
                return truck
        else:
            raise ValueError(f'Truck with id: [{id}] does not exist!')
        
    def create_scania(self, vehicle_id, name, capacity, max_range):
        scania = Scania(vehicle_id, name, capacity, max_range)
        self._trucks.append(scania)
        ApplicationData.SCANIA_NUMBER_OF_TRUCKS -= 1
        return scania
    
    def create_actros(self,vehicle_id, name, capacity, max_range):
        actros = Actros(vehicle_id, name, capacity, max_range)
        self._trucks.append(actros)
        ApplicationData.ACTROS_NUMBER_OF_TRUCKS -= 1
        return actros
    
    def create_man(self, vehicle_id, name, capacity, max_range):
        man = Man(vehicle_id,name,capacity,max_range)
        self._trucks.append(man)
        ApplicationData.MAN_NUMBER_OF_TRUCKS -= 1
        return man
    
    def create_route(self, route_id, truck_id, destinations):
        route = RouteOfTrucks(route_id, truck_id, destinations)
        return route

    def vehicle_exists(self, name) -> bool:
        return name in [this.name for this in self._trucks]