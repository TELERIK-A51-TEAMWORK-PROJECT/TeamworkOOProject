from logistics_info.location import Locations

class Customer():
    def __init__(self,location: str,first_name: str,last_name: str,telephone: str,email):
        self._location = location
        self.first_name = first_name
        self.last_name = last_name
        self.telephone = telephone
        self.email = email

    @property
    def location(self):
        return Locations.from_string(self._location)

    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self,value):
        if not value.isalpha(): 
            raise ValueError('The first name you are trying to input is not valid')
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self,value):
        if not value.isalpha(): 
            raise ValueError('The last name you are trying to input is not valid')
        self._last_name = value

    @property
    def telephone(self):
        return self._telephone
    
    @telephone.setter
    def telephone(self,value):
        allowed_characters = '0123456789'
        for char in value:
            if char not in allowed_characters:
                raise ValueError('The telephone number cannot have any other characters other than numbers')
            
        if len(value) < 10 or len(value) > 10:
            raise ValueError('The telephone you are trying to input is not valid (for australia)')
        self._telephone = value

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