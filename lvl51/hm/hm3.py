def get_european_floor(floor):
    if floor <= 0:
        return floor 
    elif floor < 13:
        return floor - 1 
    else:
        return floor - 2  
