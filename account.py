def deposite(amount):
    if amount < 0:
        print("Amount must be greater than zero")
        return 0
    else:
        return amount

def withdraw(amount,balance):
    if amount <= balance:
        return amount
    else:
        print("Insufficient balance")
        return 0

def check_balance(balance):
    print("Current Balance:",balance)

def run(balance):
    while True:
        print("1)Deposite")
        print("2)withdraw")
        print("3)Check balance")
        print("4)Exit")

        opt = input("Choose one option: ")
        if (opt == "1"):
            amount = int(input("Enter amount for deposite: "))
            a = deposite(amount)
            balance += a
            with open("account.txt","w") as file:
                file.write(f"balance {balance}")
        elif (opt == "2"):
            amount = int(input("Enter amount for withdrw: "))
            a = withdraw(amount,balance)
            balance -= a
            with open("account.txt","w") as file:
                file.write(f"balance {balance}")
        elif(opt == "3"):
            check_balance(balance)
        elif(opt == "4"):
            print("Thnks for visiting")
        else:
            print("Choose correct option")

with open("account.txt","r") as file:
    balance = file.read().split()[1]
    run(float(balance))

