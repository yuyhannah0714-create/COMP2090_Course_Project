class BankSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc):
        self.accounts[acc.accid] = acc

    def acc_withdraw(self, accid, amount):
        if accid in self.accounts:
            if self.accounts[accid].withdraw(amount):
                print(f"Withdraw successful. New balance: {self.accounts[accid].get_balance()}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid account ID!")

    def acc_deposit(self, accid, amount):
        if accid in self.accounts:
            self.accounts[accid].deposit(amount)
            print("Deposit received. Please check your balance!")
        else:
            print("Invalid account ID!")

    def transfer(self, sender, receiver, amount):
        if sender not in self.accounts or receiver not in self.accounts:
            print("Invalid account ID!")
        else:
            if self.accounts[sender].withdraw(amount):
                self.accounts[receiver].deposit(amount)
                print("Transfer completed!")
            else:
                print("Insufficient balance.")

    def get_acc_balance(self, accid):
        if accid in self.accounts:
            balance = self.accounts[accid].get_balance()
            print(f"Account {accid} balance: {balance}")
        else:
            print("Invalid account ID!")
