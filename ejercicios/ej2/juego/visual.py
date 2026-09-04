"""Dibujo puro: cada funcion dibuja una cosa, sin decidir nada."""
import pygame

from juego.constantes import (ALTO, ANCHO, COLOR_FONDO, COLOR_JUGADOR,
                              COLOR_PERDISTE, COLOR_TEXTO, COLOR_TEXTO_SUAVE,
                              COLOR_VELO, JUGADOR_CX, JUGADOR_CY, JUGADOR_RADIO)


def crear_fuentes():
    """Devuelve (fuente_hud, fuente_final, fuente_bala)."""
    return pygame.font.Font(None, 34), pygame.font.Font(None, 60), pygame.font.Font(None, 30)


def limpiar(screen):
    """Pinta el fondo."""
    screen.fill(COLOR_FONDO)


def dibujar_enemigos(screen, palabras_enemigas):
    """Dibuja los marcos con su texto."""
    for palabra in palabras_enemigas:
        palabra.dibujar(screen)


def dibujar_jugador(screen):
    """Dibuja el punto azul del jugador."""
    pygame.draw.circle(screen, COLOR_JUGADOR, (int(JUGADOR_CX), int(JUGADOR_CY)), JUGADOR_RADIO)


def dibujar_hud(screen, fuente_hud, puntos_partida, oleada_actual):
    """Dibuja la linea de oleada y puntos."""
    texto = fuente_hud.render("Oleada " + str(oleada_actual) + "   Puntos: " + str(puntos_partida), True, COLOR_TEXTO)
    screen.blit(texto, (16, 12))


def dibujar_game_over(screen, fuente_final, fuente_hud, puntos_partida, oleada_actual):
    """Dibuja la pantalla de derrota."""
    velo = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
    velo.fill(COLOR_VELO)
    screen.blit(velo, (0, 0))

    msg1 = fuente_final.render("PERDISTE", True, COLOR_PERDISTE)
    msg2 = fuente_hud.render("Puntos: " + str(puntos_partida) + "   Oleada: " + str(oleada_actual), True, COLOR_TEXTO)
    msg3 = fuente_hud.render("Enter para reiniciar - ESC para salir", True, COLOR_TEXTO_SUAVE)
    screen.blit(msg1, msg1.get_rect(center=(ANCHO / 2, ALTO / 2 - 50)))
    screen.blit(msg2, msg2.get_rect(center=(ANCHO / 2, ALTO / 2 + 10)))
    screen.blit(msg3, msg3.get_rect(center=(ANCHO / 2, ALTO / 2 + 50)))