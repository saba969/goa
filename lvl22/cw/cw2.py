user_number = int(input("enter num: "))


evens_sum = 0  
    
for i in range(user_number):
    if i % 2 == 0:
         
         evens_sum = evens_sum + 1

print(evens_sum)