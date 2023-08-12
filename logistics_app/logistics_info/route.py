from logistics_info.location import Locations
from logistics_info.calculation_helpers import calculate_destionation_km, calculate_maxrange_km
from datetime import datetime, timedelta
import math

class RouteOfTrucks:
    def __init__(self, route_id: int, truck_id: int, destinations: str, start_time: str):
        self._route_id = route_id
        self.truck_id = truck_id
        self.destinations = destinations.split('->')
        self.start_time = start_time.split('/')
        self.year = int(self.start_time[0])
        self.month = int(self.start_time[1])
        self.day = int(self.start_time[2])
        self.hours = int(10)
        self.first_date = datetime(self.year, self.month, self.day, self.hours)
        self.whole_date = datetime(self.year, self.month, self.day, self.hours)
        self.destinations_with_dates = []
        self._routes = []
        self.km = 0
        self.list_of_kms = []
        self.to_hours = []

        self.process_destinations_with_dates()
        self.calculate_km_and_maxrange()
        self.calculate_to_hours()
        self.generate_routes()
    
    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self,value):
        if value < 2023 or value> 2025:
            raise ValueError('Invalid year (must be between 2023-2025)')
        self._year = value

    @property
    def route_id(self):
        return self._route_id
    
    @route_id.setter
    def route_id(self, value):
        if value < 0:
            raise ValueError('Route id must be positive number!')
        self._route_id = value

    @property
    def routes(self):
         return self._routes

    def process_destinations_with_dates(self):
        self.destinations_with_dates = self.destinations.copy()
        self.destinations_with_dates.insert(1, self.whole_date.strftime("%m/%d/%Y, %H:%M:%S"))

    def calculate_km_and_maxrange(self):
        for current_index_location in range(len(self.destinations) - 1):
            current_location = self.destinations[current_index_location]
            self.km = calculate_destionation_km(current_location, Locations.all_locations[current_location], self.destinations, self.km)
            self.list_of_kms = calculate_maxrange_km(self.truck_id, self.list_of_kms, self.km)

    def calculate_to_hours(self):
        for kms in self.list_of_kms:
            hours = math.ceil(kms / 90)
            self.to_hours.append(hours)
            self.km = 0

    def generate_routes(self):
        start_index = 3
        for hour in self.to_hours:
            for _ in range(len(self.destinations) - 1):
                self.whole_date = self.whole_date + timedelta(hours=hour)
                self.destinations_with_dates.insert(start_index, self.whole_date.strftime("%m/%d/%Y, %H:%M:%S"))
                start_index += 2
            break

        self.routes.append([self.route_id, self.truck_id, self.destinations, self.start_time])