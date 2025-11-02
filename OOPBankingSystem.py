class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds!")
        else:
            self.balance -= amount
            print(f"✅ Withdrew {amount}. Remaining balance: {self.balance}")

acc = BankAccount("Boss", 5000)
acc.deposit(1000)
acc.withdraw(3000)
acc.withdraw(5000)
