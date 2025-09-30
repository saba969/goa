lst = [1, 546, 456, 123]
min_num = lst[0]  # დავიწყოთ სიიდან პირველი რიცხვით

for num in lst:
    if num < min_num:
        min_num = num

print([min_num])
