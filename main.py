from account import Account, SavingsAccount
from bank_system import BankSystem

def main():
    bank = BankSystem()
   
    acc1 = Account("A101", 1000)
    acc2 = SavingsAccount("S202", 5000)
    
    bank.add_account(acc1)
    bank.add_account(acc2)

    print("---bank system test---")
    bank.get_acc_balance("A101")
    bank.acc_deposit("A101", 200)
    bank.transfer("S202", "A101", 1500)
    bank.get_acc_balance("A101")
    bank.get_acc_balance("S202")

if __name__ == "__main__":
    main()
