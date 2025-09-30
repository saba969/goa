def check_age(age):
    if age >= 18:
        print(f"თქვენი ასაკი {age} - სრულწლოვანი ხართ.")
    else:
        print(f"თქვენი ასაკი {age} - არ ხართ სრულწლოვანი.")

age = int(input("შეიყვანეთ თქვენი ასაკი: "))


check_age(age)
