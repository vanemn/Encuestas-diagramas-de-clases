class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        """
        Inicializa un objeto ListadoRespuestas con un usuario y sus respuestas.

        Args:
            usuario (Usuario): El usuario que generó las respuestas.
            respuestas (list[int]): Lista de respuestas (números enteros).
        """
        self._usuario = usuario
        self._respuestas = respuestas
    # Getters
    def get_usuario(self):
        """Retorna el usuario asociado al listado de respuestas."""
        return self._usuario

    def get_respuestas(self):
        """Retorna las respuestas del listado."""
        return self._respuestas
