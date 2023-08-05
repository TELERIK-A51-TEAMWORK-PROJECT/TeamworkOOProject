from blueprints_models.company_trucks import CompanyTrucks


class Scania(CompanyTrucks):
    def __init__(self, vehicle_id: int, model_name: str, capacity_kg: int, max_range: int, number_of_vehicles: int):
        super().__init__(vehicle_id, model_name, capacity_kg, max_range, number_of_vehicles)
        ...