class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float):
        self.holder = account_holder
        self.balance = initial_balance
        
    def transfer_funds(self, other_account, amount):
        if amount <= 0:
            print("amount must be positive")
        if self.balance >= amount:
            self.balance -= amount
            other_account.balance += amount
            print(f"transferred {amount:.2f} from {self.holder} to {other_account.holder}")
        else:
            print("insufficient funds")
        
        
    def __str__(self):
        return f"Account holder: {self.holder}, Balance: {self.balance:.2f}"


person = BankAccount("David", 1000)
friend = BankAccount("Ben", 500) 

print(person)
print(friend)   
person.transfer_funds(friend, 300)
print(person)
print(friend)    