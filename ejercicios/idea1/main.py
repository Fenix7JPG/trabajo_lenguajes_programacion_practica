"""Juego de mecanografia espacial.

Ejecutar:  py -3.12 main.py   (o el python del .venv con pygame)

Estructura (paquete juego/):
- constantes: valores del juego.
- palabras: naves enemigas (PalabraObjetivo) y oleadas.
- entrada_texto: lo que escribe el jugador.
- balas: una bala por caracter correcto; destruyen al enemigo al impactar.
- sonidos: efectos de audio.
"""
import math

import pygame

from juego import balas, entrada_texto, sonidos
from juego.constantes import (ALTO, ANCHO, COLOR_FONDO, COLOR_JUGADOR,
                              COLOR_JUGADOR_BORDE, COLOR_PERDISTE,
                              COLOR_TEXTO, COLOR_TEXTO_SUAVE, COLOR_VELO, FPS,
                              JUGADOR_CX, JUGADOR_CY, JUGADOR_RADIO)
from juego.palabras import iniciar_oleada

puntos = 0
oleada = 1
game_over = False


def dibujar_jugador(screen, objetivo):
    angulo = -math.pi / 2
    if objetivo is not None:
        cx, cy = objetivo.centro()
        angulo = math.atan2(cy - JUGADOR_CY, cx - JUGADOR_CX)

    giro = angulo + math.pi / 2
    cos_g = math.cos(giro)
    sin_g = math.sin(giro)

    base = [(0, -JUGADOR_RADIO),
            (-JUGADOR_RADIO * 0.9, JUGADOR_RADIO * 0.8),
            (JUGADOR_RADIO * 0.9, JUGADOR_RADIO * 0.8)]
    puntos = []
    for px, py in base:
        puntos.append((JUGADOR_CX + px * cos_g - py * sin_g,
                       JUGADOR_CY + px * sin_g + py * cos_g))

    pygame.draw.polygon(screen, COLOR_JUGADOR, puntos)
    pygame.draw.polygon(screen, COLOR_JUGADOR_BORDE, puntos, 2)


def dibujar_hud(screen, fuente, puntos_partida, oleada_actual):
    texto = fuente.render("Oleada " + str(oleada_actual) + "   Puntos: " + str(puntos_partida), True, COLOR_TEXTO)
    screen.blit(texto, (16, 12))


def dibujar_game_over(screen, fuente_final, fuente_hud, puntos_partida, oleada_actual):
    velo = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    velo.fill(COLOR_VELO)
    screen.blit(velo, (0, 0))

    msg1 = fuente_final.render("PERDISTE", True, COLOR_PERDISTE)
    msg2 = fuente_hud.render("Puntos: " + str(puntos_partida) + "   Oleada: " + str(oleada_actual), True, COLOR_TEXTO)
    msg3 = fuente_hud.render("R o Enter para reiniciar - ESC para salir", True, COLOR_TEXTO_SUAVE)
    screen.blit(msg1, msg1.get_rect(center=(ANCHO / 2, ALTO / 2 - 50)))
    screen.blit(msg2, msg2.get_rect(center=(ANCHO / 2, ALTO / 2 + 10)))
    screen.blit(msg3, msg3.get_rect(center=(ANCHO / 2, ALTO / 2 + 50)))


def main():
    global puntos
    global oleada
    global game_over

    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Mecanografia espacial")
    clock = pygame.time.Clock()

    pygame.key.set_repeat(500, 50)

    fuente_hud = pygame.font.Font(None, 34)
    fuente_final = pygame.font.Font(None, 60)
    fuente_escrito = pygame.font.Font(None, 40)

    sonidos.cargar()

    palabras_enemigas = []
    oleada = 1
    iniciar_oleada(oleada, palabras_enemigas)

    activo = True
    while activo:
        dt = clock.tick(FPS)

        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                activo = False
            elif evento.type == pygame.KEYDOWN and game_over:
                if evento.key == pygame.K_r or evento.key == pygame.K_RETURN:
                    puntos = 0
                    oleada = 1
                    game_over = False
                    entrada_texto.reiniciar()
                    balas.reiniciar()
                    iniciar_oleada(oleada, palabras_enemigas)
                elif evento.key == pygame.K_ESCAPE:
                    activo = False

        if not game_over:
            texto = entrada_texto.actualizar_texto(eventos, palabras_enemigas)
            activa = entrada_texto.palabra_activa

            if activa is not None:
                faltan = len(texto) - activa.balas_disparadas
                for _ in range(faltan):
                    balas.disparar((JUGADOR_CX, JUGADOR_CY), activa)
                if texto == activa.texto:
                    entrada_texto.reiniciar()

            for palabra in palabras_enemigas:
                completado = ""
                if palabra is entrada_texto.palabra_activa:
                    completado = texto
                palabra.definir_completado(completado)
                palabra.actualizar(dt)

            for objetivo in balas.avanzar(dt):
                puntos = puntos + 1
                sonidos.reproducir("explosion_enemigo")

            for palabra in list(palabras_enemigas):
                if palabra.termino_muerte() == True:
                    palabras_enemigas.remove(palabra)

            for palabra in list(palabras_enemigas):
                if palabra.avanzar(dt, JUGADOR_CX, JUGADOR_CY):
                    game_over = True
                    entrada_texto.reiniciar()
                    sonidos.reproducir("explosion_jugador")
                    break

            if not palabras_enemigas:
                oleada = oleada + 1
                iniciar_oleada(oleada, palabras_enemigas)
                balas.reiniciar()

        screen.fill(COLOR_FONDO)

        for palabra in palabras_enemigas:
            palabra.dibujar(screen)

        balas.dibujar(screen)
        dibujar_jugador(screen, entrada_texto.palabra_activa)
        dibujar_hud(screen, fuente_hud, puntos, oleada)

        if entrada_texto.texto_actual != "":
            escrito = fuente_escrito.render("Escrito: " + entrada_texto.texto_actual, True, COLOR_TEXTO)
            screen.blit(escrito, escrito.get_rect(center=(ANCHO / 2, ALTO - 30)))

        if game_over:
            dibujar_game_over(screen, fuente_final, fuente_hud, puntos, oleada)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
