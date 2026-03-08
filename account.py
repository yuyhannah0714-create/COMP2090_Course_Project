class Account:
    def __init__(self, accid, balance):
        self.accid = accid
        self.__balance = balance 

    def deposit(self, amount):
    if amount <= 0:
        return False
    self.__balance += amount
    return True

  def withdraw(self, amount):
    if amount <= 0:
        return False
    if amount > self.__balance:
        return False

    self.__balance -= amount
    return True

    def get_balance(self):
        return self.__balance
class SavingsAccount(Account):
    def __init__(self, accid, balance, interest_rate=0.01):
        super().__init__(accid, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
    interest = self.__balance * self.interest_rate
    self.__balance += interest
