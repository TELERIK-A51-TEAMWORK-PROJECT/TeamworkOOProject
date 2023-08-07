from blueprints_models.company_trucks import CompanyTrucks
from blueprints_models.actros import Actros
from blueprints_models.scania import Scania
from blueprints_models.man import Man
from logistics_info.route import RouteOfTrucks
from logistics_info.customer_info import Customer
from logistics_info.package import Package

class ApplicationData:
    SCANIA_NUMBER_OF_TRUCKS = 10
    MAN_NUMBER_OF_TRUCKS = 15
    ACTROS_NUMBER_OF_TRUCKS = 15
    def __init__(self):
        self._trucks = []
        self._customers = []
        self._routes = []
        self._packages = []

    @property
    def customers(self):
        return tuple(self._customers)

    @property
    def routes(self):
        return tuple(self._routes)

    @property
    def trucks(self):
        return tuple(self._trucks)
    
    @property
    def packages(self):
        return tuple(self._packages)
    
    def find_truck_by_id(self, id) -> CompanyTrucks:
        for truck in self._trucks:
            if truck.vehicle_id == id:
                return truck
        else:
            raise ValueError(f'Truck with id: [{id}] does not exist!')
        
    def create_scania(self, vehicle_id, name, capacity, max_range):
        scania = Scania(vehicle_id, name, capacity, max_range)
        self._trucks.append(scania)
        ApplicationData.SCANIA_NUMBER_OF_TRUCKS -= 1
        return scania
    
    def create_actros(self,vehicle_id, name, capacity, max_range):
        actros = Actros(vehicle_id, name, capacity, max_range)
        self._trucks.append(actros)
        ApplicationData.ACTROS_NUMBER_OF_TRUCKS -= 1
        return actros
    
    def create_man(self, vehicle_id, name, capacity, max_range):
        man = Man(vehicle_id,name,capacity,max_range)
        self._trucks.append(man)
        ApplicationData.MAN_NUMBER_OF_TRUCKS -= 1
        return man
    
    def create_route(self, route_id, truck_id, destinations):
        route = RouteOfTrucks(route_id, truck_id, destinations)
        self._routes.append(route)
        return route
    
    def create_customer(self,locations,first_name,last_name,telephone,email):
        customer = Customer(locations,first_name,last_name,telephone,email)
        self._customers.append(customer)
        return customer
    def create_package(self,package_id, package_name, package_kg,email):
        package = Package(package_id, package_name, package_kg,email)
        self._packages.append(package)
        return package
    #Trucks
    def vehicle_exists(self,vehicle_id):
        return vehicle_id in [this.vehicle_id for this in self._trucks]
    #Routes
    def route_exits(self,route_id):
        return route_id in [this.route_id for this in self._routes]
    #Packages
    def package_exits(self,package_id):
        return package_id in [this.package_id for this in self._packages]
    
    def find_route_byid(self,id) -> RouteOfTrucks:
        for route in self._routes:
            if route.route_id == id:
                return route
        else:
            raise ValueError(f'Route with id: [{id}] does not exist!')
        
    def find_customer_byemail(self,email) -> Customer:
        for customer in self._customers:
            if customer.email == email:
                return customer
        else:
            raise ValueError(f'Customer with this email does not exist!')
        
    def find_package_byid(self,package_id) -> Package:
        for package in self._packages:
            if package.package_id == package_id:
                return package
        else:
            raise ValueError(f'Package with id: [{package_id}] does not exist!')