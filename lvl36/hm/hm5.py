def divide_two_numbers(num1, num2):
    if num2 != 0: 
        result = num1 / num2
        print(f"განაყოფი: {result}")
    else:
        print("გაფრთხილება: მეორე რიცხვი არ შეიძლება იყოს 0.")


num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

divide_two_numbers(num1, num2)
