def repeat_string(n, s):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    return s * n
result = repeat_string(3, "hello")
print(result)  

result2 = repeat_string(0, "test")
print(result2) 
