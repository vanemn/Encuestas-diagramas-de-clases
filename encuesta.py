from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas


class Encuesta:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self._preguntas = []
        self._listadosRespuestas = []

    def agregarPregunta(self, pregunta: Pregunta):
        self._preguntas.append(pregunta)

    def agregarListadoRespuestas(self, listado_respuestas):
        self._listadosRespuestas.append(listado_respuestas)

    def mostrarEncuesta(self):
        print(f"Nombre: {self.nombre}")
        for pregunta in self._preguntas:
            pregunta.mostrarPregunta()


class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edadMinima: int, edadMaxima: int):
        super().__init__(nombre)
        self.edadMinima = edadMinima
        self.edadMaxima = edadMaxima


class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, regiones: list[int]):
        super().__init__(nombre)
        self.regiones = regiones
