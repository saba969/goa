def print_odd_numbers_up_to():
  
    num = int(input("შეიყვანეთ რიცხვი: "))
    
  
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i)


print_odd_numbers_up_to()
