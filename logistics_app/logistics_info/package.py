class Package:
    def __init__(self,package_id: int, package_name: str, package_kg: int, email: str):
        self.package_id = package_id
        self.package_name = package_name
        self.package_kg = package_kg
        self.email = email

    @property
    def package_id(self):
        return self._package_id
    
    @package_id.setter
    def package_id(self,value):
        if value < 0:
            raise ValueError(f'Invalid id for package must be positive number!')
        self._package_id = value
    
    @property
    def package_name(self):
        return self._package_name
    
    @package_name.setter
    def package_name(self,value):
        if len(value) < 3 or len(value) > 25:
            raise ValueError(f'Invalid name for package')
        self._package_name = value

    @property
    def package_kg(self):
        return self._package_kg
    
    @package_kg.setter
    def package_kg(self,value):
        if value < 0 and value > 100:
            raise ValueError(f'Invalid package kilograms (too high or negative)')
        self._package_kg = value
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,value):
        allowed_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_-.'
        for char in value:
            if char not in allowed_characters:
                raise ValueError('The email you are tyring to input is invalid')
            
        if len(value) < 3 or len(value) > 25:
            raise ValueError('The email length you are trying to input is not valid')
        self._email = value