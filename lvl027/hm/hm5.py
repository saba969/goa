import random
numbers = list(range(1, 31))

num1 = random.choice(numbers)
num2 = random.choice(numbers)

product = num1 * num2

while True:
    
    user_input = input(f"Guess the product of {num1} and {num2}: ")

    
    if user_input.isdigit():
        user_guess = int(user_input)
        
        
        if user_guess == product:
            print(f"You guessed the correct product! {num1} * {num2} = {product}")
            break  
        
        else:
            print("Incorrect, Please try again")
    else:
        print("Please enter a valid number.")
