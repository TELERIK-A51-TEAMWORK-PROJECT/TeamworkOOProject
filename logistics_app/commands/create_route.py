from core.application_data import ApplicationData
from logistics_info.location import Locations
from commands.valid_helpers import try_parse_int, validate_params_count, try_parse_str


class CreateRouteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 3)
        self._params = params
        self._app_data = app_data

    def execute(self):
        route_id, truck_id, destinations = self._params
        route_id = try_parse_int(route_id)
        truck_id = try_parse_int(truck_id)
        destinations = try_parse_str(destinations)

        if not self._app_data.find_truck_by_id(truck_id):
            raise ValueError(f'No such truck with id: [{truck_id}]!')
        
        splitted_destinations = destinations.split('->')
        for current_location in splitted_destinations:
            if not Locations.from_string(current_location):
                pass

        truck = self._app_data.find_truck_by_id(truck_id)
        if self._app_data.create_route(route_id, truck_id, destinations):
            return f'Truck: [{truck_id}] {truck.model_name} with Route: [{destinations}] route id: [{route_id}] has been created!'