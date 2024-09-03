class Alternativa:
    """
    Representa una opción alternativa.
    Args:
        contenido (str): El contenido de la alternativa.
        ayuda (str, opcional): La información de ayuda para la alternativa. Por defecto, None.
    Métodos:
        mostrar(): Devuelve una representación en cadena de la alternativa.
    Atributos:
        contenido (str): El contenido de la alternativa.
        ayuda (str): La información de ayuda para la alternativa, o None si no se proporciona ayuda.
    """

    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        return f"Contenido: {self.contenido}, Ayuda: {self.ayuda if self.ayuda else 'No hay ayuda'}"
