from abc import ABC, abstractmethod

#abstracción
class Notification(ABC):
    @abstractmethod
    def send(self, message:str):
        pass
    
#Correo electrónico
class EmailNotification(Notification):
    def send(self, message:str):
        print(f"{message}")

#SMS
class SMSNotification(Notification):
    def send(self, message:str):
        print(f"{message}")

#abstraccion en vez de usar clases concretas 
class NotificationService:
    def __init__(self, notifier:Notification):
        self.notifier = notifier
        
    def notify(self, message:str):
        self.notifier.send(message)
        
email_notifier = EmailNotification()
SMS_notifier = SMSNotification()

service_email = NotificationService(email_notifier)
service_email.notify("HOLA, ESTE ES UN CORREO DE PRUEBA!")

service_sms = NotificationService(SMS_notifier)
service_sms.notify("HOLA, ESTE ES UN SMS DE PRUEBA!")
