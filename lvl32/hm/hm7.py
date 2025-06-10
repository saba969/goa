lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_sum = 0


for num in lst:
    if num % 2 != 0:
        odd_sum += num


odd_sum_list = [odd_sum] * 10

print(odd_sum_list)
