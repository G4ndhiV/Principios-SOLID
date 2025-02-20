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