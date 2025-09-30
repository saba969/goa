def count_sheep(sheep):
    return sheep.count(True)
result1 = count_sheep([True, True, False, True, False, True])
print(result1)  
result2 = count_sheep([False, False, False, False])
print(result2)

result3 = count_sheep([True, True, True, True])
print(result3)  

