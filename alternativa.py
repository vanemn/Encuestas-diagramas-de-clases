class Alternativa:
    def __init__(self, contenido, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        return f"Contenido: {self.contenido}, Ayuda: {self.ayuda if self.ayuda else 'No hay ayuda'}"
