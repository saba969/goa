lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
index = 0

while index < len(lst):
    if lst[index] % 2 == 0:
        even_numbers.append(lst[index])
    index += 1

print(even_numbers)
