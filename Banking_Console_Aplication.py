balance = 10000

while True:
    print("\nWelcome To Harshad Bank")
    print("=======Main Menu=======")
    print("Opening Balance:", balance)
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Select your Choice: ")

    if choice == "1":
        print("Current Balance Rs.", balance)

    elif choice == "2":
        amount = int(input("Enter Deposit Money: "))
        if amount > 0:
            balance = balance + amount
            print("Money Deposited Successfully...")
            print("Updated Current Balance Rs.", balance)
        else:
            print("Enter valid amount!")
    elif choice == "3":
        amount = int(input("Enter Withdraw Amount: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Withdraw Successful...")
            print("Updated Balance Rs.", balance)
        else:
            print("Insufficient Balance")
    elif choice == "4":
        print("Thank you for banking with us, Goodbye!")
        break
    else:
        print("Enter valid choice!")            