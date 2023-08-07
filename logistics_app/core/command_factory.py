from commands.create_scania import CreateScaniaCommand
from commands.create_man import CreateManCommand
from commands.create_actros import CreateActrosCommand
from commands.create_route import CreateRouteCommand
from commands.create_customer import CreateCustomerCommand
from commands.create_package import CreatePackageCommand
from commands.assign_package_to_truck import AssignPackageToTruck

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "createscania":
            return CreateScaniaCommand(params, self._app_data)
        if cmd.lower() == "createman":
            return CreateManCommand(params, self._app_data)
        if cmd.lower() == "createactros":
            return CreateActrosCommand(params, self._app_data)
        if cmd.lower() == "createroute":
            return CreateRouteCommand(params, self._app_data)
        if cmd.lower() == "createcustomer":
            return CreateCustomerCommand(params,self._app_data)
        if cmd.lower() == "createpackage":
            return CreatePackageCommand(params,self._app_data)
        if cmd.lower() == "assignpackage":
            return AssignPackageToTruck(params,self._app_data)
        
        raise ValueError(f'Invalid command name: {cmd}!')