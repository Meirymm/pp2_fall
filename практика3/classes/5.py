class Account():
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, cash):
        self.balance = self.balance+ cash

    def withdraw(self, cash):
        self.balance = self.balance-cash
        if(self.balance < 0):
            print("You have not enough money")
        else:
            print(self.balance)

wallet = Account("Meyrim", 7000)
wallet.deposit(3000)
wallet.withdraw(9000)