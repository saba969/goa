def multiples(n, limit):
    return [i for i in range(n, limit + 1, n)]


print(multiples(2, 6))  
print(multiples(3, 10)) 
print(multiples(5, 20)) 
