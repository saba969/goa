
num = int(input("enter num: "))

num1 = 0

num2 = 0

i = 0

while i < num:
    if i % 5 == 0:
        num1 = num1 + i

    elif i % 3 ==0:
        num2 = num2 +i


print(num1)
print(num2)