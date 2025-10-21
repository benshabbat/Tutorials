from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount: float) -> None:
        self.amount = amount

    @abstractmethod
    def pay(self) -> None:
        print("Processing payment")

class CreditCardPayment(Payment):
    def pay(self) -> None:
        print(f"Processing credit card payment of ${self.amount:.2f}")
    
class PayPalPayment(Payment):
    def pay(self) -> None:
        print(f"Processing PayPal payment of ${self.amount:.2f}")
        
        
class CryptoPayment(Payment):
    def pay(self) -> None:
        print(f"Processing cryptocurrency payment of ${self.amount:.2f}")        