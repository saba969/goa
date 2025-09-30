def check_positive_negative():
    
    num = float(input("შეიყვანეთ რიცხვი: "))
    
    
    if num > 0:
        print(f"{num} არის დადებითი რიცხვი.")
    elif num < 0:
        print(f"{num} არის უარყოფითი რიცხვი.")
    else:
        print("რიცხვი არის ნული.")


check_positive_negative()
