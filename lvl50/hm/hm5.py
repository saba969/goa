def move_zeros(arr):
   
    non_zeros = [x for x in arr if x != 0]
    
    zeros = len(arr) - len(non_zeros)
 
    return non_zeros + [0] * zeros
