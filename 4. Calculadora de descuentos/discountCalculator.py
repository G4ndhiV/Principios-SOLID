"""Descripción:

Este proyecto implementa un sistema de descuentos en pagos sin modificar la lógica de procesamiento de pagos. Usa el Principio Abierto/Cerrado (OCP) para permitir agregar nuevos tipos de descuentos sin alterar el código existente.

Principios SOLID aplicados:
✔ OCP: Se pueden añadir nuevas clases de descuento (VIPDiscount, NoDiscount) sin modificar la clase principal (PaymentProcessor).
✔ SRP: PaymentProcessor solo gestiona pagos, mientras que cada tipo de descuento se encarga de su propio cálculo.

Beneficio: Permite extender la funcionalidad sin cambiar código existente, reduciendo el riesgo de errores.
"""

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def calculate(self, amount):
        return amount

class VIP(PaymentProcessor):
    def calculate(self, amount):
        return amount * 0.8
    
class NoDiscount(PaymentProcessor):
    def calculate(self, amount):
        return amount
    
def main():

    vipDiscount = VIP()
    print(vipDiscount.calculate(300))
    
if __name__ == "__main__":
    main()
