def divide_numbers():
 
    num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
    num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
    
   
    if num2 == 0:
        print("მეორე რიცხვი არ უნდა იყოს 0!")
    else:
        
        result = num1 / num2
        
        print("ორივე რიცხვის გაყოფის შედეგია: {result}")


divide_numbers()
