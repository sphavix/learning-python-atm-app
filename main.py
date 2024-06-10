# Python Banking App

def show_balance(balance):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(f"Your balance is R{balance:.2f}")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

def deposit(balance):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    amount = float(input("Enter the amount to be deposited: "))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    if amount < 0:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Please make a deposit greater than 0.")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        return 0
    else:
        return amount

def withdraw(balance):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    amount = float(input("Enter the amount to be withdrawn: "))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    if amount > balance:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("You do not have enough money to withdraw, please try again.")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        return 0
    elif amount < 0:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Please enter the amount greater than zero")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        return 0
    else:
        return amount



def main():
    balance = 0
    is_running = True

    while is_running:
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("   Banking App   ")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose an option from 1 to 4: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit(balance)
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("Please choose a correct option")
            print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Thank you! have a nice day!")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

if __name__ == '__main__':
    main()