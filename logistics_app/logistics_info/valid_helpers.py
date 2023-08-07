index_location = 0

def calculate_destionation_km(location_key, location_value, destionations, km):
    global index_location
    km = 0
    if index_location == len(destionations) - 1:
         return km
    current_location = destionations[index_location]
    if location_key in destionations and location_key == destionations[index_location]:
                current_location_index = destionations.index(current_location)
                next_location = destionations[current_location_index + 1]
                for second_key, second_value in location_value.items():
                    current_location = destionations.index(location_key) #0
                    if current_location == len(destionations) - 1:
                        break
                    if second_key == next_location:
                        km += second_value
                        break
                current_location = next_location
    index_location += 1
    
    return km