balance = 0
account_created = False

while True:
    print("\n===== BANK SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # CREATE ACCOUNT
    if choice == 1:
        if account_created:
            print("Account already exists!")

        else:
            print("\n===== CREATE ACCOUNT =====")

            name = input("Enter your name: ")
            age = int(input("Enter your age: "))
            mobile = input("Enter your mobile number: ")
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))

            if age < 18:
                print("You must be 18 or older to create an account.")

            elif balance < 0:
                print("Balance cannot be negative.")

            else:
                account_created = True
                print("Account created successfully!")

    # DEPOSIT
    elif choice == 2:
        if not account_created:
            print("Please create an account first.")

        else:
            print("\n===== DEPOSIT MONEY =====")

            amount = float(input("Enter deposit amount: "))

            if amount > 0:
                balance += amount
                print("Amount deposited successfully!")
                print("New balance:", balance)
            else:
                print("Invalid amount!")

    # WITHDRAW
    elif choice == 3:
        if not account_created:
            print("Please create an account first.")

        else:
            print("\n===== WITHDRAW MONEY =====")

            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount!")

            elif amount > balance:
                print("Insufficient balance!")

            else:
                balance -= amount
                print("Amount withdrawn successfully!")
                print("Remaining balance:", balance)

    # VIEW ACCOUNT
    elif choice == 4:
        if not account_created:
            print("Please create an account first.")

        else:
            print("\n===== VIEW ACCOUNT =====")

            contact = input("Enter your contact number: ")

            if contact == mobile:
                print("\n===== ACCOUNT DETAILS =====")
                print("Name          :", name)
                print("Age           :", age)
                print("Mobile Number :", "******" + mobile[-4:])
                print("Account Number:", account_number)
                print("Balance       :", "******")

                show = input(
                    "\nDo you want to show balance? (yes/no): "
                )

                if show.lower() == "yes":
                    print("Balance:", balance)

            else:
                print("\nIncorrect contact number!")
                print("Access denied.")

    # EXIT
    elif choice == 5:
        print("\nThank you for using the Bank System!")
        print("Have a nice day!")
        break

    else:
        print("Invalid choice! Please try again.")