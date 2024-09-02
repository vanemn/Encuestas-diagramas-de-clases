from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo, edad, region):
        """
        Inicializa un objeto Usuario con correo, edad y región.

        Args:
            correo (str): Correo electrónico del usuario.
            edad (int): Edad del usuario.
            region (int): Región del usuario.
        """
        self.correo = correo
        self.edad = edad
        self.region = region

    # Getters
    def get_correo(self):
        """Retorna el correo del usuario."""
        return self.correo
    
    def get_edad(self):
        """Retorna la edad del usuario."""
        return self.edad
    
    def get_region(self):
        """Retorna la región del usuario."""
        return self.region
    
    # Setters
    def set_correo(self, correo):
        """Setea el correo del usuario."""
        self.correo = correo

    def set_edad(self, edad):
        """Setea la edad del usuario con validación."""
        if isinstance(edad, int) and edad > 0:
            self.edad = edad
        else:
            raise ValueError("La edad debe ser un número entero positivo.")
    
    def set_region(self, region):
        """Setea la región del usuario con validación."""
        if isinstance(region, int) and region > 0:
            self.region = region
        else:
            raise ValueError("La región debe ser un número entero positivo.")

    # Métodos
    def contestar_encuesta(self, respuestas):
        """
        Crea un objeto ListadoRespuestas asociado al usuario.

        Args:
            respuestas (list[int]): Lista de respuestas (números enteros).

        Returns:
            ListadoRespuestas: Instancia de ListadoRespuestas asociada al usuario.
        """
        return ListadoRespuestas(self, respuestas)
