class Pregunta:
    def __init__(self, enunciado, ayuda=None, requerida=False, alternativas=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas if alternativas else []

    def mostrar(self):
        alternativas_mostradas = [alt.mostrar() for alt in self.alternativas]
        return f"Enunciado: {self.enunciado}, Ayuda: {self.ayuda if self.ayuda else 'No hay ayuda'}, Alternativas: {alternativas_mostradas}"
