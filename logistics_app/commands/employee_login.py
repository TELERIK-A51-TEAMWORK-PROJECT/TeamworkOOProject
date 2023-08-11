from commands.valid_helpers import try_parse_str, validate_params_count
from core.application_data import ApplicationData

class EmployeeLogin:
    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        password = self._params[0]
        password = try_parse_str(password)
        access_password = "mbi10811"

        data = self._app_data

        if password != access_password:
            raise ValueError("Incorrect password! Try again!")
        
        all_trucks = []
        final_trucks = []
        
        if len(data.trucks) == 0:
            result = f'Trucks: No information\n'
        else:
            for truck in data.trucks:
                id = truck.vehicle_id
                fake_id = [id]
                copy_fake_id = fake_id.copy()
                name = str(ApplicationData.find_nameoftruck_by_id(id))
                all_trucks.append([name, str(copy_fake_id[0])])
        for truckk in all_trucks:
            joined_trucks = ' / '.join(truckk)
            final_trucks.append(joined_trucks)
        all_trucks_joined = ' ||| '.join(final_trucks)
        result = f"Trucks: {all_trucks_joined}\n"
        result += f'------------------------------------------------------------------------------\n'

        all_routes = []
        final_routes = []

        if len(data.routes) == 0:
            result += f'Routes: No information\n'
        else:
            for route in data.routes:
                route_idd = route.route_id
                fake_route_id = [route_idd]
                copy_fake_route = fake_route_id.copy()
                destinationss = '->'.join(route.destinations)
                all_routes.append([str(copy_fake_route), destinationss])
        for routess in all_routes:
            joined_routes = ' / '.join(routess)
            final_routes.append(joined_routes)
        all_routes_joined = ' ||| '.join(final_routes)
        result += f"Routes: {all_routes_joined}\n"
        result += f'------------------------------------------------------------------------------\n'

        all_packagess = []
        final_packages = []

        if len(data.packages) == 0:
            result += f'Packages: No information\n'
        else:
            for package in data.packages:
                packagee_id = package.package_id
                fake_package_id = [packagee_id]
                copy_fake_package = fake_package_id.copy()

                packagee_name = package.package_name

                packagee_kg = package.package_kg
                fake_package_kg = [packagee_kg]
                copy_fake_packagekg = fake_package_kg.copy()

                package_end_loc = package.end_location
                all_packagess.append([str(copy_fake_package), packagee_name, str(copy_fake_packagekg[0]), package_end_loc])
        for packagess in all_packagess:
            joined_packages = ' / '.join(packagess)
            final_packages.append(joined_packages)
        all_packages_joined = ' ||| '.join(final_packages)
        result += f"Packages: {all_packages_joined}\n"
        result += f'------------------------------------------------------------------------------\n'

        return result