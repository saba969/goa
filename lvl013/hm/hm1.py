number1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
number2 = float(input("შეიყვანეთ მეორე რიცხვი: "))


print("დამატება:", number1 + number2)
print("გამოკლება:", number1 - number2)
print("გამრავლება:", number1 * number2)
print("გამყოფობა:", number1 / number2 if number2 != 0 else "Cannot divide by zero")