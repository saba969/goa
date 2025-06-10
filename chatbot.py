def chatbot():
    print("გამარჯობა! მე ვარ  ჩადბოტი. თუ გსურთ საუბრის დასრულეა, დაწერეთ 'ნახვამდის'.")
    
    
    is_hello = False
    is_how_are_you = False
    is_bye = False
    is_your_name = False
    is_your_age = False
    is_best_mentor = False
    is_weather = False
    
    
    while True:
        user_input = input("თქვენ: ")
        
        
        if "გამარჯობა" in user_input or "ხო" in user_input:
            is_hello = True
            is_how_are_you = False
            is_bye = False
            is_your_name = False
            is_your_age = False
            is_best_mentor = False
            is_weather = False
            
            print("ჩადბოტი: გამარჯობა! როგორ შემიძლია დაგეხმაროთ?")
        
        
        elif "როგორ ხარ" in user_input or "როგორ ხარ?" in user_input:
            is_how_are_you = True
            is_hello = False
            is_bye = False
            is_your_name = False
            is_your_age = False
            is_best_mentor = False
            is_weather = False
            
            print("ჩადბოტი: კარგად ვარ, მადლობა რომ მკითხეთ!")

        elif "ვინ არის გოას საუკეთესო მენტორი" in user_input or "ვინ არის საუკეთესო მენტორი" in user_input:
            is_hello = False
            is_how_are_you = False
            is_bye = False
            is_your_name = False
            is_your_age = False
            is_best_mentor = True
            is_weather = False
            
            print("ჩადბოტი: ეს რა შეკითხვაა რა თქმა უნდა გაბრიელ მოლოდინი დამცინი?")

        elif "რა ამინდია დღეს" in user_input or "რა ამინდია?" in user_input:
         is_hello = False
         is_how_are_you = False
         is_bye = False
         is_your_name = False
         is_your_age = False
         is_best_mentor = False
         is_weather = True
         
         print("ჩადბოტი: გაიხედე გარეთ ვერ ხედავ რა ამინდია?!")





        

        elif "რამდენი წლის ხარ" in user_input or "რა ასაკის ხარ" in user_input or "ასაკი?" in user_input:
            is_hello = False
            is_how_are_you = False
            is_bye = False
            is_how_are_you = False
            is_your_age = True
            is_best_mentor = False
            is_weather = False
            
            print("ჩადბოტი: მე არ მაქვს ასაკი და არ ვბერდები რადგან ვარ ჩადი.")

        elif "რა არის შენი სახელი" in user_input or "რა გქვია შენ"  in user_input or "რა გქვია" in user_input:
            is_your_name = True
            is_hello = False
            is_bye = False
            is_how_are_you = False
            is_your_age = False
            is_best_mentor = False
            is_weather = False
            print("ჩადბოტი: ჩემი სახელია ჩადბოტი")

        elif  "გამოსვლა" in user_input or "თავი გამანებე" in user_input:
            is_bye = True
            is_hello = False
            is_how_are_you = False
            is_your_name = False
            is_your_age = False
            is_best_mentor = False
            is_weather = False
            
            print("ჩადბოტი: ნახვამდის! კარგ დღეს გისურვებთ!")
            break
            

        
                 
        


        
        

    
            
        
        
        elif not is_hello and not is_how_are_you and not is_bye and not is_your_name and not is_best_mentor and not is_weather and not is_your_age and not is_weather and not is_your_age:
            print("ჩადბოტი: ბოდიში, ვერ გავიგე თქვენი შეკითხვა. შეგიძლიათ გაახმოვანოთ სხვა სიტყვებით?")
        
        

if __name__ == "__main__":
    chatbot()