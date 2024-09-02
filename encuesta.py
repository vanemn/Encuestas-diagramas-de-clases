from pregunta import Pregunta


class Encuesta:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._preguntas = []
        self._listadosRespuestas = []

    def agregarPregunta(self, pregunta: Pregunta):
        self._preguntas.append(pregunta)
