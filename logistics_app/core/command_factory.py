from commands.create_truck import CreateTruckCommand
from commands.create_route import CreateRouteCommand
from commands.create_customer import CreateCustomerCommand
from commands.create_package import CreatePackageCommand
from commands.assign_package_to_truck import AssignPackageToTruck
from commands.employee_login import EmployeeLogin
from commands.manager_login import ManagerLogin

class CommandFactory:
    def __init__(self, data):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()

        if cmd.lower() == "createtruck":
            return CreateTruckCommand(params, self._app_data)
        if cmd.lower() == "createroute":
            return CreateRouteCommand(params, self._app_data)
        if cmd.lower() == "createcustomer":
            return CreateCustomerCommand(params,self._app_data)
        if cmd.lower() == "createpackage":
            return CreatePackageCommand(params,self._app_data)
        if cmd.lower() == "assignpackage":
            return AssignPackageToTruck(params,self._app_data)
        if cmd.lower() == "employeelogin":
            return EmployeeLogin(params, self._app_data)
        if cmd.lower() == "managerlogin":
            return ManagerLogin(params, self._app_data)
        
        raise ValueError(f'This command: [{cmd}] doesn\'t exist!')