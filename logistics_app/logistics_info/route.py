from blueprints_models.truck_models import Truck_Models
from logistics_info.location import Locations
from logistics_info.valid_helpers import calculate_destionation_km
from datetime import date, datetime, timedelta
import math

class RouteOfTrucks:
    def __init__(self, route_id: int, truck_id: int, destinations, start_time: str):
        self.route_id = route_id
        self.truck_id = truck_id
        self.destinations = destinations.split('->') #[sydney, melbourne, perith]
        self.destinations_with_dates = self.destinations.copy()
        self.start_time = start_time.split('/')     # [2023, 7, 8]
        self.year = int(self.start_time[0])
        self.month = int(self.start_time[1])
        self.day = int(self.start_time[2])
        self.hours = int(10)
        self.first_date = datetime(self.year, self.month, self.day, self.hours)
        self.whole_date = datetime(self.year, self.month, self.day, self.hours)
        self.destinations_with_dates.insert(1, self.whole_date.strftime("%m/%d/%Y, %H:%M:%S"))
        self._routes = [] #[route_id, truck_id, dest]
        self.km = 0
        self.list_of_kms = [] # [877, 3509]
        self.to_hours = []

        for key_current_location, value in Locations.all_locations.items():
           last_elements = self.destinations[-1]
           last_index = self.destinations.index(last_elements)
           if len(self.list_of_kms) == len(self.destinations) - 1:
               break
           self.km = calculate_destionation_km(key_current_location, value, self.destinations, self.km) #Изчислява километрите на даденият маршрут
           self.list_of_kms.append(self.km)
        for kms in self.list_of_kms:
            kms /= 90
            ceiled = math.ceil(kms)
            self.to_hours.append(ceiled)
            self.km = 0  #[10, 39]
        start_index = 3
        for hour in self.to_hours:
            for _ in range(len(self.destinations) - 1):
                self.whole_date = self.whole_date + timedelta(hours=hour)
                self.destinations_with_dates.insert(start_index, self.whole_date.strftime("%m/%d/%Y, %H:%M:%S"))
                start_index += 2
            break

        self.routes.append([self.route_id, self.truck_id, self.destinations, self.start_time])
                            # 1                 1001       ['Sydney', [data na sydney], 'Melbourne', 'Alice Springs']

    @property
    def routes(self):
        return self._routes