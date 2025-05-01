class bank:
    def __init__(self,name):
        self.name=name
        self.accounts={}
    def create_acc(self,acc_number,customer_name,initial_balance=0):
        if acc_number in self.accounts:
            print("Account already exist")
        else:
            self.accounts[acc_number]={"customer_name":customer_name,"balance":initial_balance}
            print(f"Account created for {customer_name} with balance {initial_balance}")
    def deposit(self,acc_number,amount):
        if acc_number not in self.accounts:
            print("Account not found")
        else:
            self.accounts[acc_number]['balance']+=amount
            print(f" Deposited {amount}. New Balance = {self.accounts[acc_number]['balance']}")
    def withdraw(self,acc_number,amount):
        if acc_number not in self.accounts:
            print("Account not found")
        else:
            self.accounts[acc_number]['balance']-=amount
            print(f" Withdrew {amount}. New Balance = {self.accounts[acc_number]['balance']}")
    def check_balance(self,acc_number):
        if acc_number not in self.accounts:
            print("Account not found")
        else:
            print(f"Balance for {self.accounts[acc_number]['customer_name']} : {self.accounts[acc_number]['balance']}")
    def transfer(self,from_account,to_account,amount):
        if from_account not in self.accounts or to_account not in self.accounts:
            print("One or both accounts not found")
        elif self.accounts[from_account]['balance']<amount:
            print("Insufficient Balance")
        else:
            self.accounts[from_account]['balance']-=amount
            self.accounts[to_account]['balance']+=amount
            print(f" Transferres {amount} from {from_account} to {to_account}")  
Bank=bank("MyBank") 
while True:
    print("\n1. Create account\n2. Deposit \n3. Withdraw\n4. Check bakance\n5. Transfer\n6. Exit")
    choice= int (input("Enter choice:-"))
    if choice == 1:
        acc_number = input("Enter account number: ")
        customer_name = input("Enter customer name: ")
        initial_balance = float(input("Enter initial balance: "))
        Bank.create_acc(acc_number, customer_name, initial_balance)

    elif choice == 2:
        acc_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        Bank.deposit(acc_number, amount)

    elif choice == 3:
        acc_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        Bank.withdraw(acc_number, amount)

    elif choice == 4:
        acc_number = input("Enter account number: ")
        Bank.check_balance(acc_number)

    elif choice == 5:
        from_account = input("Enter from account number: ")
        to_account = input("Enter to account number: ")
        amount = float(input("Enter amount to transfer: "))
        Bank.transfer(from_account, to_account, amount)

    elif choice == 6:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

        