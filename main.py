from alternativa import Alternativa
from pregunta import Pregunta
from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from usuario import Usuario
from listado_respuestas import ListadoRespuestas

def main():
    # Crear alternativas
    alternativa1 = Alternativa("Alternativa 1", "Esta es la primera alternativa.")
    alternativa2 = Alternativa("Alternativa 2", "Esta es la segunda alternativa.")

    pregunta1 = Pregunta("¿Cuál es tu color favorito?", "Selecciona tu color favorito.", False, [alternativa1, alternativa2])

    encuesta = Encuesta("Encuesta de Preferencias")
    encuesta._preguntas.append(pregunta1) 

    usuario = Usuario(correo="user@usuario.com" , edad=20, region=1)
    print (f"Usuario:{usuario.correo} {usuario.edad} {usuario.region}")
    respuestas = [1]
    usuario.contestar_encuesta(encuesta,respuestas)

    print(f"Encuesta:{encuesta.mostrarEncuesta()}\n" )
   
    # Crear una encuesta limitada por edad

    encuesta_limitada_edad = EncuestaLimitadaEdad("Encuesta de Preferencias", 18, 60)
    encuesta_limitada_edad._preguntas.append(pregunta1)
    usuario.contestar_encuesta(encuesta_limitada_edad,respuestas)
    print(f"Encuesta Limitada por Edad:{encuesta_limitada_edad.mostrarEncuesta()}\n" )

    # Crear una encuesta limitada por región
    encuesta_limitada_region = EncuestaLimitadaRegion("Encuesta de Preferencias", [1, 2, 3])
    encuesta_limitada_region._preguntas.append(pregunta1)
    usuario.contestar_encuesta(encuesta_limitada_region,respuestas)
    print(f"Encuesta Limitada por Región:{encuesta_limitada_region.mostrarEncuesta()}\n" )

    

if __name__ == "__main__":
    main()