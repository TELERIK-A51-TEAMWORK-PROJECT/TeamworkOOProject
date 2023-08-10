from core.application_data import ApplicationData
from commands.valid_helpers import try_parse_int, validate_params_count, try_parse_str
from logistics_info.package_status import PackageStatus

#Todo...
class AssignPackageToTruck:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 3) #truck_id, route_id, package_id
        self._params = params
        self._app_data = app_data


    def execute(self):
        truck_id, route_id, package_id = self._params
        truck_id = try_parse_int(truck_id)
        route_id = try_parse_int(route_id)
        package_id = try_parse_int(package_id)

        truck = self._app_data.find_truck_by_id(truck_id) #1003
        route = self._app_data.find_route_byid(route_id)
        package = self._app_data.find_package_byid(package_id)
        customer = self._app_data.find_customer_byemail(package.email)
        start_location = customer.location
        end_location = package.end_location

        current_status = package.package_status #[OPEN]
        destinations = route.routes[0][2]

        
        
        for _ in route.routes:
            
            for _ in destinations: #[Sydney]

                index_start_location = destinations.index(start_location)
                index_end_location = destinations.index(end_location)

                if index_start_location < index_end_location:
                    result_dates = []
                    for i, item in enumerate(route.destinations_with_dates):
                        if i % 2 == 1:
                            result_dates.append(f"({item})")
                        else:
                            result_dates.append(item)
                        if i < len(route.destinations_with_dates) - 2:
                            result_dates.append("->")
                            result_dates.pop(-1)
                            
                    formatted_dates = ""
                    for item in result_dates:
                        if item.startswith('('):
                            formatted_dates += item + ' | '
                            continue
                        else:
                            formatted_dates += item + '->'
                    formatted_dates = formatted_dates.rstrip(',| ')
                        

                    result = f'Package [{package_id}] has been assigned to truck:\n'
                    result += f'Truck Info: [{truck_id}] {ApplicationData.find_nameoftruck_by_id(truck_id)}\n'
                    result += f'Current route: {" -> ".join(destinations)}\n'
                    result += f'Departure time - Expected delivery time in different locations: {formatted_dates}\n'
        #CAPACITY CALCS
        if truck.capacity_kg == 0: 
            raise ValueError(f'No space left in the truck {truck_id} {ApplicationData.find_nameoftruck_by_id(truck_id)} assign package to another truck')
        truck.capacity_kg -= package.package_kg
        result += f'Kilograms left on the truck: ({truck.capacity_kg})\n'
        result += f'Status: {PackageStatus.advance_status(current_status)}\n'
        result += f'------------------------------------------------------------------------------'
        return result