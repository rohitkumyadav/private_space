class Account:
    def __init__(self,balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def auth_debit(self,amount):
        self.balance -= amount
        print(f"Rupees {amount} is debit")
        print(f"Total amount : {self.total_Amount()}")

    def auth_credit(self, amount):
        self.balance +=amount
        print(f"Rupees {amount} is credit")
        print(f"Total amount : {self.total_Amount()}")

    def total_Amount(self):
        return self.balance

    def amount_left(self):
        print("Total: ",self.balance)



a1 = Account(20000,98787879)
a1.amount_left()
a1.auth_debit(1000)
a1.auth_credit(200000000)