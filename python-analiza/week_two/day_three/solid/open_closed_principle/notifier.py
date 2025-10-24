
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
    def __init__(self, device_token: str):
        self.device_token = device_token
    def send(self, message: str) -> None:
        print(f"Sending push notification to {self.device_token}: {message}")
        
notify_sms = SMSNotifier()
notify_sms.send("Hello via SMS!")        
notify_push = PushNotifier("device_token_123")
notify_push.send("Hello via Push Notification!")

notify_email = EmailNotifier()
notify_email.send("Hello via Email!")


