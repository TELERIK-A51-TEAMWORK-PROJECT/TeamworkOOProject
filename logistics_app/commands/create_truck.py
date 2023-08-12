from core.application_data import ApplicationData
from commands.valid_helpers import try_parse_int, validate_params_count

class CreateTruckCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 3)
        self._params = params
        self._app_data = app_data

    def execute(self):
        vehicle_id,capacity,max_range = self._params
        capacity = try_parse_int(capacity)
        max_range = try_parse_int(max_range)
        vehicle_id = try_parse_int(vehicle_id)

        if self._app_data.vehicle_exists(vehicle_id):
            raise ValueError(f'Truck {ApplicationData.find_nameoftruck_by_id(vehicle_id)} with id: [{vehicle_id}] already exists!')
        self._app_data.create_truck(vehicle_id,capacity,max_range)

        result = f'------------------------------------------------------------------------------\n'
        result += f'Truck {ApplicationData.find_nameoftruck_by_id(vehicle_id)} with id: [{vehicle_id}] was created!\n'
        result += f'------------------------------------------------------------------------------'
        return result