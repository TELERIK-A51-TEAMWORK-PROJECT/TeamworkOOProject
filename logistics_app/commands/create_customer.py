from core.application_data import ApplicationData
from commands.valid_helpers import try_parse_int, validate_params_count,try_parse_str
from logistics_info.location import Locations

class CreateCustomerCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        locations,first_name,last_name,telephone,email = self._params
        locations = Locations.from_string(locations)
        first_name = try_parse_str(first_name)
        last_name = try_parse_str(last_name)
        
        self._app_data.create_customer(locations,first_name,last_name,telephone,email)

        return f'In {locations} customer: {first_name} {last_name} with number: {telephone} and email: {email} was created!'
