from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        return 'Transportandote'
    
class TransportService:
    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
    
    def transport(self):
        return self.vehicle.move()

class Car(Vehicle):
    def move(self):
        return "El coche está conduciendo"

class Bicycle(Vehicle):
    def move(self):
        return "La bicicleta está pedaleando"

if __name__ == "__main__":
    car = Car()
    bicycle = Bicycle()
    
    car_service = TransportService(car)
    bicycle_service = TransportService(bicycle)
    
    print(car_service.transport())  
    print(bicycle_service.transport()) 