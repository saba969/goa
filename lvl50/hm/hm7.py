def check_limit(arr, limit):
  
    for num in arr:
        if num > limit:
            return False
    return True
