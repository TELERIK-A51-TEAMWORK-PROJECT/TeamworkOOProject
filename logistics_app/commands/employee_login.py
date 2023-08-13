from commands.valid_helpers import try_parse_str, validate_params_count
from core.application_data import ApplicationData

class EmployeeLogin:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        password = try_parse_str(self._params[0])
        access_password = "mbi10811" #Access pass
        
        if password != access_password:
            raise ValueError("Incorrect password! Try again!")

        data = self._app_data

        result = 'EMPLOYEE VIEW INFO:\n'

        result += self.format_data(data.trucks, "Trucks", lambda truck: truck.vehicle_id, lambda truck: [str(ApplicationData.find_nameoftruck_by_id(truck.vehicle_id))])

        result += self.format_data(data.routes, "Routes", lambda route: route.route_id, lambda route: ['->'.join(route.destinations)])

        result += self.format_data(data.packages, "Packages", lambda package: package.package_id, lambda package: [package.package_name, str(package.package_kg), package.end_location])

        result += f'------------------------------------------------------------------------------\n'
        return result
    
    def format_data(self, data_list, data_type, id_func, info_func):
        formatted_data = []

        if len(data_list) == 0:
            return f'{data_type} (0):\nNo information\n'
        else:
            for index, item in enumerate(data_list, start=1):
                item_id = id_func(item)
                item_info = info_func(item)
                formatted_item_info = ' - '.join(item_info)
                formatted_data.append(f"{index}. ID: {item_id} - {formatted_item_info}")

        total_counts = len(data_list)
        all_items_joined = '\n'.join(formatted_data)
        return f"Total {data_type} ({total_counts}):\n{all_items_joined}\n"