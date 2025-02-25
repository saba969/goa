def reverse_digits(n):
    return [int(digit) for digit in str(n)[::-1]]
result1 = reverse_digits(12345)
print(result1)  

result2 = reverse_digits(987)
print(result2)  

result3 = reverse_digits(0)
print(result3) 