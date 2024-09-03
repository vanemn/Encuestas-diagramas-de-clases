from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False, alternativas: Alternativa = None):
        """
        Inicializa una instancia de la clase Pregunta.

        Parámetros:
        - enunciado (str): El enunciado de la pregunta.
        - ayuda (str, opcional): La ayuda o explicación adicional para la pregunta. Por defecto es None.
        - requerida (bool, opcional): Indica si la pregunta es requerida o no. Por defecto es False.
        - alternativas (Alternativa, opcional): Las alternativas posibles para la pregunta. Por defecto es None.
        """
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas

    def mostrarPregunta(self):
        """
        Muestra la pregunta junto con su enunciado, ayuda y alternativas.

        Returns:
            str: Una cadena de texto que contiene el enunciado de la pregunta, la ayuda (si está disponible) y las alternativas.
        """
        alternativas_mostradas = [alt.mostrar() for alt in self.alternativas]
        return f"Enunciado: {self.enunciado}, Ayuda: {self.ayuda if self.ayuda else 'No hay ayuda'}, Alternativas: {alternativas_mostradas}"
