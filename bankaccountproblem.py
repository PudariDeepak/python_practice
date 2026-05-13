#program to specify how to check balance,withdraw and deposite money from the bank
def deposite(amount):
    if amount>0:
        print(amount,"credited Successfully!")
        return amount
    else:
        print("Amount must be greater than 0.")
        return 0
    
def withdraw(amount,balance):
    if amount<=balance:
        print(amount,"debited successfully!")
        return amount 
    else:
        print("Insufficient Balance.")
        return 0

def check_balance( balance):
    print("Current Balance:",balance)

def run(balance):
    while True:
        print("1) Deposite")
        print("2) Withdraw")
        print("3) Check balance")
        print("4) Exit")
        opt = input("Choose one Option: ")
        if opt=="1":
            amount = float(input("Enter a amount for deposite: "))
            balance+=deposite(amount)
            input("Click on Enter for continue...")
        elif opt=="2":
            amount = float(input("Enter a amount for withdraw: "))
            balance-=withdraw(amount,balance)
            input("Click on Enter for continue...")
        elif opt=="3":
            check_balance(balance)
            input("Click on Enter for continue...")
        elif opt=="4":
            print("Thanks for visiting.")
            break
        else:
            print("Choose correct option")

balance=0.0
pin = 9419

chances = 1
while chances<=3:
    user_pin = int(input("Enter a pin: "))
    if user_pin == pin:
        run(balance)
        break
    chances+=1
    print("Wrong pin.")
if chances==4:
    print("Try After one hour")