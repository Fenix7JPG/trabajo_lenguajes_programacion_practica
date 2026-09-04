"""Juego de mecanografia espacial. Ejecutar:  py -3.12 main.py

Aqui vive el estado y el bucle; los modulos de juego/ son funciones puras.
"""
import pygame

from juego import balas, entrada_texto, visual
from juego.constantes import ANCHO, ALTO, FPS, JUGADOR_CX, JUGADOR_CY
from juego.palabras import iniciar_oleada


def creacion_oleada(n):
    """Estado limpio para una oleada nueva: (texto, activa, balas, enemigos)."""
    enemigos = iniciar_oleada(n)
    return "", None, [], enemigos


def decision_game_over(eventos):
    """Teclas del game over: devuelve "reiniciar" (Enter), "salir" (ESC) o None."""
    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_RETURN:
                return "reiniciar"
            if evento.key == pygame.K_ESCAPE:
                return "salir"
    return None


def main():
    # estado del juego: SOLO vive aqui dentro
    puntos = 0
    oleada = 1
    game_over = False

    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mecanografia espacial")
    clock = pygame.time.Clock()

    pygame.key.set_repeat(500, 50)

    fuente_hud, fuente_final, fuente_bala = visual.crear_fuentes()

    palabras_enemigas = []
    texto = ""
    activa = None
    balas_jugador = []
    oleada = 1
    texto, activa, balas_jugador, palabras_enemigas = creacion_oleada(oleada)

    activo = True
    while activo:
        dt = clock.tick(FPS)

        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                activo = False

        if game_over == True:
            decision = decision_game_over(eventos)
            if decision == "salir":
                activo = False
            elif decision == "reiniciar":
                puntos = 0
                oleada = 1
                game_over = False
                texto, activa, balas_jugador, palabras_enemigas = creacion_oleada(oleada)

        if not game_over:
            texto, activa = entrada_texto.actualizar_texto(eventos, palabras_enemigas, texto, activa)

            if activa is not None:
                faltan = len(texto) - activa.balas_disparadas
                nuevas = texto[len(texto) - faltan:]
                for caracter in nuevas:
                    balas_jugador = balas.disparar(balas_jugador, (JUGADOR_CX, JUGADOR_CY), activa, caracter)

            # pintar el verde ANTES de soltar la palabra (asi queda congelado)
            for palabra in palabras_enemigas:
                completado = ""
                if palabra is activa:
                    completado = texto
                palabra.definir_completado(completado)
                palabra.actualizar(dt)

            # soltar la palabra despues de pintar su verde
            if activa is not None and texto == activa.texto:
                texto = ""
                activa = None

            balas_jugador, destruidas = balas.avanzar(balas_jugador, dt)
            puntos = puntos + len(destruidas)

            sobrevivientes = []
            for palabra in palabras_enemigas:
                if palabra.termino_muerte() == False:
                    sobrevivientes.append(palabra)
            palabras_enemigas = sobrevivientes

            for palabra in palabras_enemigas:
                if palabra.avanzar(dt, JUGADOR_CX, JUGADOR_CY) == True:
                    game_over = True
                    texto = ""
                    activa = None
                    break

            if not palabras_enemigas:
                oleada = oleada + 1
                texto, activa, balas_jugador, palabras_enemigas = creacion_oleada(oleada)

        visual.limpiar(screen)
        visual.dibujar_enemigos(screen, palabras_enemigas)
        balas.dibujar(screen, balas_jugador, fuente_bala)
        visual.dibujar_jugador(screen)
        visual.dibujar_hud(screen, fuente_hud, puntos, oleada)

        if game_over == True:
            visual.dibujar_game_over(screen, fuente_final, fuente_hud, puntos, oleada)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()