while True:
    try:
        user_input = input("Enter a number (or -1 to exit): ")
        
        if user_input.strip() == "":
            print("Please enter a valid number.")
            continue
            
        decimal = int(user_input)
        
        if decimal == -1:
            break
            
        if decimal < 0:
            print("Please enter a positive decimal number.")
            continue

        if decimal == 0:
            print("Binary equivalent: 0")
            continue

        binary = ""
        temp = decimal
        
        while temp > 0:
            remainder = temp % 2
            binary = str(remainder) + binary
            temp = temp // 2

        print("Binary equivalent:", binary)
        
    except ValueError:
        print("Invalid input! Please enter an integer number only.")
