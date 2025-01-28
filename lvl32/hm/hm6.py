lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0

for num in lst:
    if num % 2 == 0:
        even_sum += num


even_sum_list = [even_sum] * 10

print(even_sum_list)
