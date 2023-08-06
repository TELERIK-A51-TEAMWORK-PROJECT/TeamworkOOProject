from core.application_data import ApplicationData
from blueprints_models.truck_models import Truck_Models
from commands.valid_helpers import try_parse_int, validate_params_count


class CreateScaniaCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 4)
        self._params = params
        self._app_data = app_data

    def execute(self):
        vehicle_id,name,capacity,max_range = self._params
        name = Truck_Models.from_string(name)
        capacity = try_parse_int(capacity)
        max_range = try_parse_int(max_range)
        vehicle_id = try_parse_int(vehicle_id)

        if self._app_data.vehicle_exists(name):
            raise ValueError(f'Truck Scania with id: [{vehicle_id}] already exists!')
        self._app_data.create_scania(vehicle_id,name,capacity,max_range)

        return f'Truck Scania with id: [{vehicle_id}] was created!'