lst = [1, 2, 3, 4, 5]
reversed_lst = []
index = len(lst) - 1

while index >= 0:
    reversed_lst.append(lst[index])
    index -= 1

print(reversed_lst)
