"2.- Sistema de Pagos"
"Descripción:"

"Este proyecto implementa un sistema de pagos desacoplado de los métodos específicos (PayPalPayment, CreditCardPayment). Usa el Principio de Inversión de Dependencias (DIP) para que el sistema dependa de una abstracción (Payment) en lugar de clases concretas."

"Principios SOLID aplicados:"
"✔ DIP: PaymentSystem depende de Payment en lugar de implementaciones específicas."
"✔ SRP: PaymentSystem solo gestiona el proceso de pago, mientras que cada método de pago (PayPalPayment, CreditCardPayment) maneja su propia lógica."

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class PayPalPayment(Payment):
    def process_payment(self, amount: float):
        print(f"Procesando pago de ${amount:.2f} con PayPal.")

class CreditCardPayment(Payment):
    def process_payment(self, amount: float):
        print(f"Procesando pago de ${amount:.2f} con Tarjeta de Crédito.")

class PaymentSystem:
    def __init__(self, payment_method: Payment):
        self.payment_method = payment_method

    def make_payment(self, amount: float):
        self.payment_method.process_payment(amount)

if __name__ == "__main__":
    paypal = PayPalPayment()
    credit_card = CreditCardPayment()

    payment_system = PaymentSystem(paypal)
    payment_system.make_payment(100.0)

    payment_system = PaymentSystem(credit_card)
    payment_system.make_payment(250.0)
