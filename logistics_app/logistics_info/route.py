from blueprints_models.truck_models import Truck_Models
from logistics_info.location import Locations

class RouteOfTrucks:
    def __init__(self, route_id: int, truck_id: int, destinations: str):
        self.route_id = route_id
        self.truck_id = truck_id
        self.destinations = destinations.split('->')
        self.routes = []
        self.km = 0

        for key_current_location, value in Locations.all_locations.items():
            if 'SYD' in destinations and key_current_location == 'SYD':
                for second_key, second_value in value.items():
                    current_location = self.destinations.index(key_current_location)
                    if current_location == len(self.destinations) - 1:
                        break
                    next_location = self.destinations[current_location + 1]
                    if second_key == next_location:
                        self.km += second_value
                    current_location = second_key
            if 'MEL' in destinations and key_current_location == 'MEL':
                for second_key, second_value in value.items():
                    current_location = self.destinations.index(key_current_location)
                    if current_location == len(self.destinations) - 1:
                        break
                    next_location = self.destinations[current_location + 1]
                    if second_key == next_location:
                        self.km += second_value
                    current_location = second_key
            if 'ADL' in destinations and key_current_location == 'ADL':
                for second_key, second_value in value.items():
                    current_location = self.destinations.index(key_current_location)
                    if current_location == len(self.destinations) - 1:
                        break
                    next_location = self.destinations[current_location + 1]
                    if second_key == next_location:
                        self.km += second_value
                    current_location = second_key
            if 'ASP' in destinations and key_current_location == 'ASP':
                for second_key, second_value in value.items():
                    current_location = self.destinations.index(key_current_location)
                    if current_location == len(self.destinations) - 1:
                        break
                    next_location = self.destinations[current_location + 1]
                    if second_key == next_location:
                        self.km += second_value
                    current_location = second_key
            if 'BRI' in destinations and key_current_location == 'BRI':
                for second_key, second_value in value.items():
                    current_location = self.destinations.index(key_current_location)
                    if current_location == len(self.destinations) - 1:
                        break
                    next_location = self.destinations[current_location + 1]
                    if second_key == next_location:
                        self.km += second_value
                    current_location = second_key
            if 'DAR' in destinations and key_current_location == 'DAR':
                for second_key, second_value in value.items():
                    current_location = self.destinations.index(key_current_location)
                    if current_location == len(self.destinations) - 1:
                        break
                    next_location = self.destinations[current_location + 1]
                    if second_key == next_location:
                        self.km += second_value
                    current_location = second_key
            if 'PER' in destinations and key_current_location == 'PER':
                for second_key, second_value in value.items():
                    current_location = self.destinations.index(key_current_location)
                    if current_location == len(self.destinations) - 1:
                        break
                    next_location = self.destinations[current_location + 1]
                    if second_key == next_location:
                        self.km += second_value
                    current_location = second_key


        self.routes.append([self.route_id, self.truck_id, self.destinations])
                            # 1                 1001       ['SYD', 'MEL', 'ASP']