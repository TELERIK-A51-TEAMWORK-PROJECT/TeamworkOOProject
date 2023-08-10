from logistics_info.location import Locations

index_location = 0
if_perith = 0

def calculate_destionation_km(location_key, location_value, destionations, km):
    global index_location
    global if_perith
    
    km = 0
    #TODO
    if location_key == Locations.PER:
        if_perith += 1
    if index_location == len(destionations) - 1:
         return km
    if if_perith > 1:
        current_location = destionations[index_location - 1] #[adelide, mel]
    else:
        current_location = destionations[index_location]

    while current_location != destionations[-1]:
        if location_key in destionations and location_key == destionations[index_location]:
            current_location_index = destionations.index(current_location)
            next_location = destionations[current_location_index + 1]
            for second_key, second_value in location_value.items():
                current_location = destionations.index(location_key) #0
                if current_location == len(destionations) - 1:
                    break
                if second_key == next_location:
                    km += second_value
                    index_location += 1
                    return km
            current_location = next_location
        break

#Max_range calcs

def calculate_maxrange_km(truck_id, list_of_kms, km):
     #Scania
    if truck_id >= 1001 and truck_id <= 1010:
        if km == None:
            pass
        else:
            list_of_kms.append(km)
        if sum(list_of_kms) > 8000:
            list_of_kms = []
            raise ValueError(f'Exceeding max range of Scania [{truck_id}]!')
    #Man
    if truck_id >= 1011 and truck_id <= 1025:
        if km == None:
            pass
        else:
            list_of_kms.append(km)
        if sum(list_of_kms) > 10000:
            list_of_kms = []
            raise ValueError(f'Exceeding max range of Man [{truck_id}]!')
    if truck_id >= 1026 and truck_id <= 1040:
        if km == None:
            pass
        else:
            list_of_kms.append(km)
        if sum(list_of_kms) > 13000:
            list_of_kms = []
            raise ValueError(f'Exceeding max range of Actros [{truck_id}]!')
        
    return list_of_kms

     