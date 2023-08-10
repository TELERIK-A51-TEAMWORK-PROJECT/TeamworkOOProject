class Locations:
    SYD = "Sydney"
    syd_distance = {
        'Sydney': '',
        'Melbourne': 877,
        'Adelaide': 1376,
        'AliceSprings': 2762,
        'Brisbane': 909,
        'Darwin': 3935,
        'Perth': 4016
    }
    MEL = "Melbourne"
    mel_distance = {
        'Sydney': 877,
        'Melbourne': '',
        'Adelaide': 725,
        'AliceSprings': 2255,
        'Brisbane': 1765,
        'Darwin': 3752,
        'Perth': 3509
    }
    ADL = "Adelaide"
    adl_distance = {
        'Sydney': 1376,
        'Melbourne': 725,
        'Adelaide': '',
        'AliceSprings': 1530,
        'Brisbane': 1927,
        'Darwin': 3027,
        'Perth': 2785
    }
    ASP = "AliceSprings"
    asp_distance = {
        'Sydney': 2762,
        'Melbourne': 2255,
        'Adelaide': 1530,
        'AliceSprings': '',
        'Brisbane': 2993,
        'Darwin': 1497,
        'Perth': 2481
    }
    BRI = "Brisbane"
    bri_distance = {
        'Sydney': 909,
        'Melbourne': 1765,
        'Adelaide': 1927,
        'AliceSprings': 2993,
        'Brisbane': '',
        'Darwin': 3426,
        'Perth': 4311
    }
    DAR = "Darwin"
    dar_distance = {
        'Sydney': 3935,
        'Melbourne': 3752,
        'Adelaide': 3027,
        'AliceSprings': 1497,
        'Brisbane': 3426,
        'Darwin': '',
        'Perth': 4025
    }
    PER = "Perth"
    per_distance = {
        'Sydney': 4016,
        'Melbourne': 3509,
        'Adelaide': 2785,
        'AliceSprings': 2481,
        'Brisbane': 4311,
        'Darwin': 4025,
        'Perth': ''
    }

    all_locations = {
        'Sydney': syd_distance,
        'Melbourne': mel_distance,
        'Adelaide': adl_distance,
        'AliceSprings': asp_distance,
        'Brisbane': bri_distance,
        'Darwin': dar_distance,
        'Perth': per_distance
    }

    @classmethod
    def from_string(cls, location):
        if location not in [cls.SYD, cls.MEL, cls.ADL, cls.ASP, cls.BRI, cls.DAR, cls.PER]:
            raise ValueError(f'There is no {location} in the Australian region')

        return location