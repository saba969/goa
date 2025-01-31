
def add(a, b):
    result = a + b
    print("ჯამი:", a, "+", b, "=", result)


def subtract(a, b):
    result = a - b
    print("გამოკლება:", a, "-", b, "=", result)


def multiply(a, b):
    result = a * b
    print("გამრავლება:", a, "*", b, "=", result)


def divide(a, b):
    if b != 0:   
        result = a / b
        print("გაყოფა:", a, "/", b, "=", result)
    else:
        print("გაყოფა ვერ ხორციელდება 0-ით!")
