from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount: float) -> None:
        self.amount = amount

    @abstractmethod
    def pay(self) -> None:
        print(f"Processing payment of ${self.amount:.2f}")

class CreditCardPayment(Payment):
    def pay(self) -> None:
        print(f"Processing credit card payment of ${self.amount:.2f}")
    
class PayPalPayment(Payment):
    def pay(self) -> None:
        print(f"Processing PayPal payment of ${self.amount:.2f}")
        
        
class CryptoPayment(Payment):
    def __init__(self, amount: float, wallet_address: str) -> None:
        super().__init__(amount)
        self.wallet_address = wallet_address
    def pay(self) -> None:
        print(f"Processing cryptocurrency payment of ${self.amount:.2f} to wallet {self.wallet_address}")        