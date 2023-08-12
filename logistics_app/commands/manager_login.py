from commands.valid_helpers import try_parse_str, validate_params_count
from core.application_data import ApplicationData
from commands.data_formatter import format_data

class ManagerLogin:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        password = self._params[0]
        password = try_parse_str(password)
        access_password = "manager1000" #Access pass

        data = self._app_data

        if password != access_password:
            raise ValueError("Incorrect password! Try again!")
        
        result = 'MANAGER VIEW INFO:\n'
        result += format_data(data.customers, "Customers", lambda customer: customer.location,lambda customer: [customer.first_name, customer.last_name, customer.telephone, customer.email])

        result += f'------------------------------------------------------------------------------\n'
        return result