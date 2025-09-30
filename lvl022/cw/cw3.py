
number = int(input("შეიყვანეთ რიცხვი: "))

even_sum = 0
odd_sum = 0


for i in range(1, number + 1):
    if i % 2 == 0:
        even_sum += 1
    else:  
        odd_sum += i



