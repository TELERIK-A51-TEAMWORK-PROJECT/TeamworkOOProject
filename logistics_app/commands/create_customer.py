from core.application_data import ApplicationData
from commands.valid_helpers import validate_params_count,try_parse_str
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

        result = f'Customer was created in ({locations}):\n'
        result +=f'Info: [{first_name} {last_name}] | Number: [{telephone}] | Email: ({email})\n'
        result +=f'------------------------------------------------------------------------------'
        return result
