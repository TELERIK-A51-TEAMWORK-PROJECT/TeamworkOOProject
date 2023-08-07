class Locations:
    SYD = "Sydney"
    syd_distance = {
        'SYD': '',
        'MEL': 877,
        'ADL': 1376,
        'ASP': 2762,
        'BRI': 909,
        'DAR': 3935,
        'PER': 4016
    }
    MEL = "Melbourne"
    mel_distance = {
        'SYD': 877,
        'MEL': '',
        'ADL': 725,
        'ASP': 2255,
        'BRI': 1765,
        'DAR': 3752,
        'PER': 3509
    }
    ADL = "Adelaide"
    adl_distance = {
        'SYD': 1376,
        'MEL': 725,
        'ADL': '',
        'ASP': 1530,
        'BRI': 1927,
        'DAR': 3027,
        'PER': 2785
    }
    ASP = "AliceSprings"
    asp_distance = {
        'SYD': 2762,
        'MEL': 2255,
        'ADL': 1530,
        'ASP': '',
        'BRI': 2993,
        'DAR': 1497,
        'PER': 2481
    }
    BRI = "Brisbane"
    bri_distance = {
        'SYD': 909,
        'MEL': 1765,
        'ADL': 1927,
        'ASP': 2993,
        'BRI': '',
        'DAR': 3426,
        'PER': 4311
    }
    DAR = "Darwin"
    dar_distance = {
        'SYD': 3935,
        'MEL': 3752,
        'ADL': 3027,
        'ASP': 1497,
        'BRI': 3426,
        'DAR': '',
        'PER': 4025
    }
    PER = "Perth"
    per_distance = {
        'SYD': 4016,
        'MEL': 3509,
        'ADL': 2785,
        'ASP': 2481,
        'BRI': 4311,
        'DAR': 4025,
        'PER': ''
    }

    all_locations = {
        'SYD': syd_distance,
        'MEL': mel_distance,
        'ADL': adl_distance,
        'ASP': asp_distance,
        'BRI': bri_distance,
        'DAR': dar_distance,
        'PER': per_distance
    }

    @classmethod
    def from_string(cls, location):
        if location not in [cls.SYD, cls.MEL, cls.ADL, cls.ASP, cls.BRI, cls.DAR, cls.PER]:
            raise ValueError(f'There is no {location} in the Australian region')

        return location