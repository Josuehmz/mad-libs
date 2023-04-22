import random

# Lista de historias con espacios en blanco para rellenar
historias = [
    "Un día, mi [adjetivo] amigo y yo decidimos ir a [verbo] en el [lugar].",
    "Cuando era joven, me encantaba [verbo] en el [lugar] con mis [familiares/amigos].",
    "Mi [adjetivo] comida es [comida].",
    "Siempre me siento [adjetivo] cuando escucho [música].",
    "Mi [adjetivo] animal es el/la [animal].",
]

# Función para pedir palabras al usuario y reemplazar en la historia
def rellenar_historia(historia):
    palabras = []
    # Obtener lista de palabras necesarias
    for palabra in historia.split():
        if palabra.startswith("[") and palabra.endswith("]"):
            tipo = palabra[1:-1]
            ingreso = input(f"Ingrese un(a) {tipo}: ")
            palabras.append(ingreso)
        else:
            palabras.append(palabra)
    # Unir palabras en la historia completada
    historia_completa = " ".join(palabras)
    return historia_completa

# Función principal del juego
def jugar():
    continuar = True
    while continuar:
        # Seleccionar una historia al azar
        historia = random.choice(historias)
        # Pedir al usuario que rellene la historia
        historia_completa = rellenar_historia(historia)
        print("\nHistoria completa:\n")
        print(historia_completa)
        # Preguntar si el usuario desea continuar jugando
        respuesta = input("\n¿Desea jugar de nuevo? (s/n): ")
        if respuesta.lower() == "n":
            continuar = False

# Main del programa
if __name__ == "__main__":
    jugar()