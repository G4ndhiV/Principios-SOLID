# Principios-SOLID


1.- Gestión de Notificaciones
Descripción:
Este proyecto permite enviar notificaciones por diferentes medios (correo electrónico y SMS) sin acoplarse a una implementación específica. Utiliza el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP) para asegurar que la lógica de notificación y el servicio que la usa estén desacoplados.

Principios SOLID aplicados:
✔ SRP: Cada clase tiene una única responsabilidad (Notificación y Servicio de Notificación).
✔ DIP: El servicio depende de una abstracción (Notification) y no de clases concretas (EmailNotification, SMSNotification).

Beneficio: Es fácil agregar nuevos tipos de notificación sin modificar el servicio principal.

 

2.- Sistema de Pagos
Descripción:

Este proyecto implementa un sistema de pagos desacoplado de los métodos específicos (PayPalPayment, CreditCardPayment). Usa el Principio de Inversión de Dependencias (DIP) para que el sistema dependa de una abstracción (Payment) en lugar de clases concretas.

Principios SOLID aplicados:
✔ DIP: PaymentSystem depende de Payment en lugar de implementaciones específicas.
✔ SRP: PaymentSystem solo gestiona el proceso de pago, mientras que cada método de pago (PayPalPayment, CreditCardPayment) maneja su propia lógica.

 

3.- Gestión de Envíos y Seguimiento de Paquetes
Descripción:

Este proyecto implementa un sistema para gestionar una empresa de logística que maneja envíos y seguimiento de paquetes. En este sistema, existen diferentes roles:

Transportista: Se encarga únicamente de transportar paquetes.
Administrador de Rutas: Optimiza rutas y supervisa el estado de los envíos.
Soporte al Cliente: Maneja consultas y actualizaciones sobre el estado de los paquetes.
Aplicación del Principio de Segregación de Interfaces (ISP):
Se crean interfaces específicas según las responsabilidades de cada rol:

Trackable: Para realizar el seguimiento de los paquetes.
Deliverable: Para manejar entregas y transportes de paquetes.
Routable: Para optimizar rutas y gestionar logística.
De esta forma, cada rol implementa solo los métodos que necesita sin verse obligado a implementar funcionalidades innecesarias.

 

4.- Calculadora de Descuentos
Descripción:

Este proyecto implementa un sistema de descuentos en pagos sin modificar la lógica de procesamiento de pagos. Usa el Principio Abierto/Cerrado (OCP) para permitir agregar nuevos tipos de descuentos sin alterar el código existente.

Principios SOLID aplicados:
✔ OCP: Se pueden añadir nuevas clases de descuento (VIPDiscount, NoDiscount) sin modificar la clase principal (PaymentProcessor).
✔ SRP: PaymentProcessor solo gestiona pagos, mientras que cada tipo de descuento se encarga de su propio cálculo.

Beneficio: Permite extender la funcionalidad sin cambiar código existente, reduciendo el riesgo de errores.

5.- Sistema de Vehículos
Descripción:
Este sistema permite a un servicio de transporte usar diferentes vehículos de manera genérica. Implementa el Principio de Sustitución de Liskov (LSP), asegurando que cualquier tipo de vehículo (Car, Bicycle) pueda sustituir a la clase base (Vehicle) sin causar problemas.

Principios SOLID aplicados:
✔ LSP: Car y Bicycle heredan de Vehicle y pueden usarse sin modificar el código del servicio de transporte.
✔ DIP: TransportService depende de la abstracción Vehicle, no de clases concretas.

Beneficio: Facilita la adición de nuevos tipos de vehículos sin modificar la lógica de transporte.
