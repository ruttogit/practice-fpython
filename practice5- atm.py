balance = 5000
user_input = ""
user_widthrawals = 0

while True:
    print(f" 1. Check balance \n 2. Withdraw money\n 3. Exit")
    user_input = input()
    if user_input == "1":
        print(f"Your balance is: Ksh {balance}")
    elif user_input == "2":
        user_widthrawals = int(input(f"Enter withdrawal amount: "))
        if user_widthrawals > 0 and balance >= user_widthrawals:
            balance -= user_widthrawals
            print(balance)
            print("Withdrawal successful!")
            print(f"Remaining balance: KSh {balance}")

    elif user_input == "3":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid option")
    
    
    