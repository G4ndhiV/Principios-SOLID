""" Descripción:
Este sistema permite a un servicio de transporte usar diferentes vehículos de manera genérica. Implementa el Principio de Sustitución de Liskov (LSP), asegurando que cualquier tipo de vehículo (Car, Bicycle) pueda sustituir a la clase base (Vehicle) sin causar problemas.

Principios SOLID aplicados:
✔ LSP: Car y Bicycle heredan de Vehicle y pueden usarse sin modificar el código del servicio de transporte.
✔ DIP: TransportService depende de la abstracción Vehicle, no de clases concretas.

Beneficio: Facilita la adición de nuevos tipos de vehículos sin modificar la lógica de transporte.
"""



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
