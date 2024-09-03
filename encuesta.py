from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas


class Encuesta:
    """
    Clase que representa una encuesta.

    Métodos:
        agregarPregunta(pregunta: Pregunta): Agrega una pregunta a la encuesta.
        agregarListadoRespuestas(listado_respuestas): Agrega un listado de respuestas a la encuesta.
        mostrarEncuesta(): Muestra el nombre de la encuesta y las preguntas asociadas.
    """

    def __init__(self, nombre: str):
        """
        Metodo constructor que Inicializa una nueva instancia de Encuesta.

        Args:
            nombre (str): El nombre de la encuesta.

        Atributos:
        nombre (str): El nombre de la encuesta.
        _preguntas (list): Lista de preguntas que forman parte de la encuesta.
        _listadosRespuestas (list): Lista de listados de respuestas asociadas a la encuesta.
        """
        self.nombre = nombre
        self._preguntas = []
        self._listadosRespuestas = []

    def agregarPregunta(self, pregunta: Pregunta):
        """
        Agrega una pregunta a la encuesta.

        Args:
            pregunta (Pregunta): La pregunta que se desea agregar.
        """
        self._preguntas.append(pregunta)

    def agregarListadoRespuestas(self, listadorespuestas: ListadoRespuestas):
        """
        Agrega un listado de respuestas a la encuesta.

        Args:
            listado_respuestas (ListadoRespuestas): El listado de respuestas que se desea agregar.
        """
        self._listadosRespuestas.append(listadorespuestas)

    def mostrarEncuesta(self):
        """
        Muestra el nombre de la encuesta y las preguntas asociadas.
        """
        preguntas_mostradas = [preg.mostrarPregunta() for preg in self._preguntas]
        respuestas_mostradas = [resp.get_respuestas() for resp in self._listadosRespuestas]
        return f"Nombre: {self.nombre}, Preguntas: {preguntas_mostradas}, Respuestas: {respuestas_mostradas}"


class EncuestaLimitadaEdad(Encuesta):
    """
    Clase que representa una encuesta limitada por un rango de edad.

    """

    def __init__(self, nombre: str, edadMinima: int, edadMaxima: int):
        """
        Inicializa una nueva instancia de EncuestaLimitadaEdad.

        Args:
            nombre (str): El nombre de la encuesta.
            edadMinima (int): La edad mínima requerida para participar.
            edadMaxima (int): La edad máxima permitida para participar.
        """
        super().__init__(nombre)
        self.edadMinima = edadMinima
        self.edadMaxima = edadMaxima


class EncuestaLimitadaRegion(Encuesta):
    """
    Clase que representa una encuesta limitada por regiones.

    """

    def __init__(self, nombre: str, regiones: list[int]):
        """
        Inicializa una nueva instancia de EncuestaLimitadaRegion.

        Args:
            nombre (str): El nombre de la encuesta.
            regiones (list[int]): Lista de identificadores de las regiones permitidas para participar.
        """
        super().__init__(nombre)
        self.regiones = regiones
