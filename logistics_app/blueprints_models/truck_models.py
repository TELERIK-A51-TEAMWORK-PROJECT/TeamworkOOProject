
class Truck_Models:
    SCANIA = 'Scania'
    MAN = 'Man'
    ACTROS = 'Actros'

    @classmethod
    def from_string(cls, models_of_trucks):
        if models_of_trucks not in [cls.SCANIA, cls.MAN,cls.ACTROS]:
            raise ValueError(f'None of the possible Truck values matches the value {models_of_trucks}.')

        return models_of_trucks