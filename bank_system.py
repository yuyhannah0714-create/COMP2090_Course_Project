from account import Account, SavingsAccount
from max_heap import MaxHeap

class BankSystemWithHeap:
    def __init__(self):
        self.accounts = {}
        self.balance_heap = MaxHeap()
    
    def add_account(self, acc):
        self.accounts[acc.accid] = acc
        self.balance_heap.push(acc.accid, acc.get_balance())
    
    def acc_withdraw(self, accid, amount):
        if accid in self.accounts:
            account = self.accounts[accid]
            if account.withdraw(amount):
                new_balance = account.get_balance()
                print(f"Withdraw successful. New balance: {new_balance}")
                self.balance_heap.update_balance(accid, new_balance)
                return True
            else:
                print("Insufficient balance.")
                return False
        else:
            print("Invalid account ID!")
            return False
    
    def acc_deposit(self, accid, amount):
        if accid in self.accounts:
            account = self.accounts[accid]
            if account.deposit(amount):
                new_balance = account.get_balance()
                print(f"Deposit received. New balance: {new_balance}")
                self.balance_heap.update_balance(accid, new_balance)
                return True
            else:
                print("Invalid deposit amount!")
                return False
        else:
            print("Invalid account ID!")
            return False
    
    def transfer(self, sender, receiver, amount):
        if sender not in self.accounts or receiver not in self.accounts:
            print("Invalid account ID!")
            return False
        else:
            sender_account = self.accounts[sender]
            receiver_account = self.accounts[receiver]
            
            if sender_account.withdraw(amount):
                receiver_account.deposit(amount)
                self.balance_heap.update_balance(sender, sender_account.get_balance())
                self.balance_heap.update_balance(receiver, receiver_account.get_balance())
                
                print("Transfer completed!")
                return True
            else:
                print("Insufficient balance.")
                return False
    
    def get_acc_balance(self, accid):
        if accid in self.accounts:
            balance = self.accounts[accid].get_balance()
            print(f"Account {accid} balance: {balance}")
            return balance
        else:
            print("Invalid account ID!")
            return None
    
    def get_top_customers_by_balance(self, n=5):
        print(f"\n=== Top {n} Customers by Balance ===")
        top_customers = self.balance_heap.get_top_n(n)
        
        if not top_customers:
            print("No accounts in the system.")
            return []
        
        for i, (balance, accid) in enumerate(top_customers, 1):
            account_type = "Savings" if isinstance(self.accounts[accid], SavingsAccount) else "Regular"
            print(f"{i}. Account {accid}: ${balance:.2f} ({account_type} Account)")
        
        return top_customers
    
    def serve_priority_customer(self):
        if self.balance_heap.is_empty():
            print("No customers to serve.")
            return None
        
        top_customer = self.balance_heap.peek()
        if top_customer:
            balance, accid = top_customer
            print(f"\n=== Serving Priority Customer ===")
            print(f"Account ID: {accid}")
            print(f"Balance: ${balance:.2f}")
            print("Offering premium financial advice...")
            return accid
        return None
    
    def display_all_accounts_sorted(self):
        print("\n=== All Accounts Sorted by Balance (Descending) ===")
        
        temp_heap = MaxHeap()
        for accid, account in self.accounts.items():
            temp_heap.push(accid, account.get_balance())
        
        sorted_accounts = []
        while not temp_heap.is_empty():
            sorted_accounts.append(temp_heap.pop())
        
        for i, (balance, accid) in enumerate(sorted_accounts, 1):
            account_type = "Savings" if isinstance(self.accounts[accid], SavingsAccount) else "Regular"
            print(f"{i}. Account {accid}: ${balance:.2f} ({account_type} Account)")
        
        return sorted_accounts


if __name__ == "__main__":
    bank = BankSystemWithHeap()
    bank.add_account(Account("A001", 1000))
    bank.add_account(SavingsAccount("A002", 2500, interest_rate=0.02))

    bank.acc_deposit("A001", 300)
    bank.acc_withdraw("A002", 400)
    bank.transfer("A001", "A002", 150)

    bank.get_acc_balance("A001")
    bank.get_acc_balance("A002")

    bank.get_top_customers_by_balance(2)
    bank.display_all_accounts_sorted()
