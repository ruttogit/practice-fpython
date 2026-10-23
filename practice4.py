password = "python123"

input_pass = input(f"Enter your password: ")

while password != "python123":
    print("Wrong password! Try again.")
    break
else:
    print("Access granted!")