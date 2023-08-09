from core.application_data import ApplicationData
from commands.valid_helpers import try_parse_int, validate_params_count, try_parse_str

#Todo
class CreatePackageCommand:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 4)
        self._params = params
        self._app_data = app_data

    def execute(self):
        package_id,package_name,package_kg,email = self._params
        package_id = try_parse_int(package_id)
        package_name = try_parse_str(package_name)
        package_kg = try_parse_int(package_kg)


        customer = self._app_data.find_customer_byemail(email)

        if self._app_data.package_exits(package_id):
            raise ValueError(f'Package with id: [{package_id}] alredy exists!')
        self._app_data.create_package(package_id, package_name, package_kg, email)

        package = self._app_data.find_package_byid(package_id)
        result = f'Package has been created with id: [{package_id}] Status: [{package.package_status}]\n'
        result += f'Info of package: Name: {package_name} | Kilograms: {package_kg} | Customer Email: ({customer.email})\n'
        result += f'Wating for truck to pick up..\n'
        result += f'------------------------------------------------------------------------------'
        return result