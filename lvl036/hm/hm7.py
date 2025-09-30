def check_positive_or_negative(num):
    if num > 0:
        print(f"{num} არის დადებითი რიცხვი.")
    elif num < 0:
        print(f"{num} არის უარყოფითი რიცხვი.")
    else:
        print(f"{num} არის ნულოვანი რიცხვი.")


num = float(input("შეიყვანეთ რიცხვი: "))

check_positive_or_negative(num)
