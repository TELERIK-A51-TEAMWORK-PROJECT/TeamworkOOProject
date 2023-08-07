from blueprints_models.truck_models import Truck_Models
from logistics_info.location import Locations
from logistics_info.valid_helpers import calculate_destionation_km

class RouteOfTrucks:
    def __init__(self, route_id: int, truck_id: int, destinations: str):
        self.route_id = route_id
        self.truck_id = truck_id
        self.destinations = destinations.split('->')
        self.routes = []
        self.km = 0

        for key_current_location, value in Locations.all_locations.items():
           self.km += calculate_destionation_km(key_current_location, value, self.destinations, self.km) #Изчислява километрите на даденият маршрут
 
        self.routes.append([self.route_id, self.truck_id, self.destinations])
                            # 1                 1001       ['SYD', 'MEL', 'ASP']