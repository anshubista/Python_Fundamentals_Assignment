def classify_number():
   while True:
        # Prompt the user to enter a number or type "exit" to stop
        user_input = input("Please enter a number : ")
        if user_input.lower() == "exit":
            print("Exiting the number classification.")
            break
        try:
            number = float(user_input)
            
            # Classify the number as positive, negative, or zero
            if number > 0:
                print("The number is positive.")
            elif number < 0: 
                print("The number is negative.")
            else:
                print("The number is zero.")
classify_number()