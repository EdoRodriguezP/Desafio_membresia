from abc import ABC, abstractmethod

# Clase abstracta base para todas las membresías
class Membresia(ABC):
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        
        # Encapsulamiento de los atributos
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    # Propiedad para acceder al correo del suscriptor
    @property
    def correo_suscriptor(self):
        return self.__correo_suscriptor
    
    # Propiedad para acceder al número de tarjeta
    @property
    def numero_tarjeta(self):
        return self.__numero_tarjeta

    # Método abstracto para cambiar de tipo de membresía
    @abstractmethod
    def cambiar_suscripcion(self, nueva_membresia: int) -> "Membresia":
        pass

# Interfaz para membresías que pueden ser canceladas
class Cancelable(ABC):
    @abstractmethod
    def cancelar_suscripcion(self):
        pass
    
    
# Interfaz para membresías con control parental
class Control_parental(ABC):
    @abstractmethod
    def modificar_control_parental(self):
        pass

# Interfaz para membresías con contenido sin conexión
class Contenido_maxSin_conexion(ABC):    
    @abstractmethod
    def incrementar_contenido_sin_conexion(self):
        pass

# Función para crear una nueva membresía según el tipo solicitado
def _crear_nueva_membresia(self, nueva_membresia: int) -> Membresia:
    if nueva_membresia == 1:
        return Basico(self.correo_suscriptor, self.numero_tarjeta)    
    elif nueva_membresia == 2:
        return Familiar(self.correo_suscriptor, self.numero_tarjeta)            
    elif nueva_membresia == 3:
        return Sin_conexion(self.correo_suscriptor, self.numero_tarjeta)          
    elif nueva_membresia == 4:
        return Pro(self.correo_suscriptor, self.numero_tarjeta)
    else:
        return self  # Si el tipo no es válido, retorna la membresía actual

# Clase para membresía Gratis
class Gratis(Membresia):
    costo = 0
    dispositivos = 1

    # Permite cambiar a cualquier tipo de membresía válida
    def cambiar_suscripcion(self, nueva_membresia: int) -> Membresia:
        if nueva_membresia in [1, 2, 3, 4]:
            return _crear_nueva_membresia(self, nueva_membresia)
        return self

# Clase para membresía Básica
class Basico(Membresia):
    costo = 3000
    dispositivos = 2

    # Permite cambiar solo a Familiar, Sin_conexion o Pro
    def cambiar_suscripcion(self, nueva_membresia: int) -> Membresia:
        if nueva_membresia in [2, 3, 4]:
            return _crear_nueva_membresia(self, nueva_membresia)
        return self
    # Cancela la suscripción y retorna una membresía Gratis
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

# Clase para membresía Familiar
class Familiar(Membresia, Control_parental):
    costo = 5000
    dispositivos = 5
    
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self._dias_regalo = 7  # Días de regalo al crear la membresía
    
        # Propiedad para acceder a los días de regalo
        @property
        def dias_regalo(self):
            return self.__dias_regalo
    # Permite cambiar solo a Basico, Sin_conexion o Pro
    def cambiar_suscripcion(self, nueva_membresia: int) -> Membresia:
        if nueva_membresia in [1, 3, 4]:
            return _crear_nueva_membresia(self, nueva_membresia)
        return self
    
    # Método declarado, lógica pendiente
    def modificar_control_parental(self):
        pass
    
    # Cancela la suscripción y retorna una membresía Gratis
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

# Clase para membresía Sin Conexión
class Sin_conexion(Membresia, Contenido_maxSin_conexion):
    costo = 3500
    dispositivos = 2
    
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.__dias_regalo = 7  # Días de regalo al crear la membresía
    
    # Propiedad para acceder a los días de regalo
    @property    
    def dias_regalo(self):
        return self.__dias_regalo
    
    # Permite cambiar solo a Basico, Familiar o Pro
    def cambiar_suscripcion(self, nueva_membresia: int) -> Membresia:
        if nueva_membresia in [1, 2, 4]:
            return _crear_nueva_membresia(self, nueva_membresia)
        return self
    
    # Método declarado, lógica pendiente
    def incrementar_contenido_sin_conexion(self):
        pass
    
    # Cancela la suscripción y retorna una membresía Gratis
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

# Clase para membresía Pro
class Pro(Membresia, Control_parental, Contenido_maxSin_conexion):
    costo = 7000
    dispositivos = 6
    
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        super().__init__(correo_suscriptor, numero_tarjeta)
        self.__dias_regalo = 15  # Días de regalo al crear la membresía
    
    # Propiedad para acceder a los días de regalo    
    @property
    def dias_regalo(self):
        return self.__dias_regalo

    # Permite cambiar solo a Basico, Familiar o Sin_conexion
    def cambiar_suscripcion(self, nueva_membresia: int) -> Membresia:
        if nueva_membresia in [1, 2, 3]:
            return _crear_nueva_membresia(self, nueva_membresia)
        return self
    
    # Método declarado, lógica pendiente
    def modificar_control_parental(self):
        pass
    
    # Método declarado, lógica pendiente
    def incrementar_contenido_sin_conexion(self):
        pass
    
    # Cancela la suscripción y retorna una membresía Gratis
    def cancelar_suscripcion(self):
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)

