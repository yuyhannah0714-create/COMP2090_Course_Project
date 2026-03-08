from account import Account, SavingsAccount
from bank_system import BankSystem

bank = BankSystem()

a = Account("1", 1000)
b = SavingsAccount("2", 5000)

bank.add_account(a)
bank.add_account(b)

print("test")

bank.get_acc_balance("1")

bank.acc_deposit("1",200)

bank.transfer("2","1",1500)

print("after transfer")

bank.get_acc_balance("1")
bank.get_acc_balance("2")

print("done")
