import random

def recomendar_pelicula(genero):
    """Recomienda una película según el género indicado. y en diferente orden"""
    peliculas = {
        "accion": ["Rapidos y Furiosos", "John Wick", "Redentor"],
        "comedia": ["Doble vida", "6 ridiculos", "MR. Bean"],
        "ciencia ficcion": ["Interstellar", "Things", "Matrix", "Gladiador"]
    }
    
    genero = genero.lower()
    if genero in peliculas:
        return random.choice(peliculas[genero])
    else:
        return "Género no encontrado. Intente con acción, comedia, ciencia ficción."

if __name__ == "__main__":
    print("Agente de Recomendación de Películas")
    genero_usuario = input("Ingrese su género favorito: ")
    recomendacion = recomendar_pelicula(genero_usuario)
    print("Película recomendada:", recomendacion)
