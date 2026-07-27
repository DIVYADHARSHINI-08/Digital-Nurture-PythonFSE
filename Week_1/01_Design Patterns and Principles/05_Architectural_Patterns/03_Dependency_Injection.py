from abc import ABC, abstractmethod


class MessageService(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailService(MessageService):
    def send(self, message):
        print(f"Email Sent: {message}")


class Notification:
    def __init__(self, service):
        self.service = service

    def notify(self, message):
        self.service.send(message)


email = EmailService()
notification = Notification(email)

notification.notify("Welcome to Cognizant!")