"""Constantes del juego: ventana, colores, jugador y pools de palabras."""

ANCHO = 960
ALTO = 540
FPS = 60

COLOR_FONDO = (30, 30, 30)
COLOR_TEXTO = (255, 255, 255)
COLOR_TEXTO_SUAVE = (200, 200, 200)
COLOR_PERDISTE = (220, 30, 30)
COLOR_VELO = (0, 0, 0, 160)
COLOR_JUGADOR = (40, 120, 220)
COLOR_JUGADOR_BORDE = (180, 230, 255)

JUGADOR_CX = ANCHO / 2
JUGADOR_CY = ALTO / 2
JUGADOR_RADIO = 22

POOL_FACIL = ["sol", "luz", "mar", "pan", "red", "ojo", "pez", "tio"]
POOL_MEDIA = ["arbol", "nieve", "queso", "playa", "monte",
              "viento", "nube", "rio", "flor", "azul"]
POOL_DIFICIL = ["cancion", "corazon", "azucar", "telefono", "murcielago",
                "avion", "camion", "leccion", "musica", "numero",
                "rapido", "dificil", "buho", "dia"]
