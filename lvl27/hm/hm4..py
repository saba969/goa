
numbers = list(range(1, 31))

chosen_index = 10 

while True:
    
    user_input = input("Please guess the index (1-30): ")

    
    if user_input.isdigit():
        user_guess = int(user_input)
        
        
        if user_guess < 1 or user_guess > 30:
            print("Incorrect, You must enter a number from 1 to 30")
        
