
from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        print("Sending message...")

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending email notification: {message}")

class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending SMS notification: {message}")

class PushNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f"Sending push notification: {message}")