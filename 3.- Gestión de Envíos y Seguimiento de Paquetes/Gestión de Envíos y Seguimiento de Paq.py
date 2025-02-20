# Gestión de Envíos y Seguimiento de Paquetes

"""Descripción:

Este proyecto implementa un sistema para gestionar una empresa de logística que maneja envíos y seguimiento de paquetes. En este sistema, existen diferentes roles:

Transportista: Se encarga únicamente de transportar paquetes.
Administrador de Rutas: Optimiza rutas y supervisa el estado de los envíos.
Soporte al Cliente: Maneja consultas y actualizaciones sobre el estado de los paquetes.
Aplicación del Principio de Segregación de Interfaces (ISP):
Se crean interfaces específicas según las responsabilidades de cada rol:

Trackable: Para realizar el seguimiento de los paquetes.
Deliverable: Para manejar entregas y transportes de paquetes.
Routable: Para optimizar rutas y gestionar logística.
De esta forma, cada rol implementa solo los métodos que necesita sin verse obligado a implementar funcionalidades innecesarias."""




from abc import ABC, abstractmethod

class Trackable(ABC):
    @abstractmethod
    def track_package(self, package_id: str) -> str:
        pass

class Deliverable(ABC):
    @abstractmethod
    def deliver_package(self, package_id: str) -> str:
        pass

class Routable(ABC):
    @abstractmethod
    def optimize_route(self) -> str:
        pass

class Transportista(Deliverable):
    def deliver_package(self, package_id: str) -> str:
        return f"el paquete {package_id} fue entregado."

class AdministradorRutas(Routable):
    def optimize_route(self) -> str:
        return "La ruta fue modificada por el admin. de rutas."

class SoporteCliente(Trackable):
    def track_package(self, package_id: str) -> str:
        return f"El estado del paquete {package_id} se ha desplegado para el soporte técnico."







def main():
    transportista = Transportista()
    administrador = AdministradorRutas()
    soporte = SoporteCliente()
    
    print(transportista.deliver_package("0000000"))
    print(administrador.optimize_route())
    print(soporte.track_package("0000000"))

if __name__ == "__main__":
    main()
