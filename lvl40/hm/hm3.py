def what_century(year):
    return (year - 1) // 100 + 1
result1 = what_century(100)  
print(result1)  

result2 = what_century(101)  
print(result2)  

result3 = what_century(2005)  
print(result3)  

result4 = what_century(2023)  
print(result4) 