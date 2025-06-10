def check_even_or_odd(num):
    if num % 2 == 0:
        print(f"{num} არის ლუწი რიცხვი.")
    else:
        print(f"{num} არის კენტი რიცხვი.")

num = int(input("შეიყვანეთ რიცხვი: "))

check_even_or_odd(num)
