def list_difference(a, b):
    
    b_set = set(b)
   
    return [x for x in a if x not in b_set]
