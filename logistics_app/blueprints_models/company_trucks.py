class CompanyTrucks:
    def __init__(self, vehicle_id: int, model_name: str, capacity_kg: int, max_range: int, number_of_vehicles: int):
        self.vehicle_id = vehicle_id
        self.model_name = model_name
        self.capacity_kg = capacity_kg
        self.max_range = max_range
        self.number_of_vehicles = number_of_vehicles

    
    #всички видове проверки дали е негативно число макс килограми и т.н