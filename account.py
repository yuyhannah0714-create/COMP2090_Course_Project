class Account:
    def __init__(self, accid, balance):
        self.accid = accid
        self.__balance = balance 

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance
class SavingsAccount(Account):
    def __init__(self, accid, balance, interest_rate=0.01):
        super().__init__(accid, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
