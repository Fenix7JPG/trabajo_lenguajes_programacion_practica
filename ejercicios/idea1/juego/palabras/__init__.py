"""Enemigos: PalabraObjetivo y generacion de oleadas.

Cada PalabraObjetivo es una nave enemiga con una etiqueta de texto.
Se acerca al jugador. Cada caracter correcto le envia una bala; el enemigo
se destruye cuando recibe un impacto por cada caracter de su palabra.
"""
import math
import random

import pygame

from juego.constantes import (ALTO, ANCHO, POOL_DIFICIL, POOL_FACIL,
                              POOL_MEDIA)


def lerp_color(color_a, color_b, factor):
    factor = max(0.0, min(1.0, factor))
    return tuple(int(a + (b - a) * factor) for a, b in zip(color_a, color_b))


def _posicion_borde():
    margen = 30
    lado = random.randint(0, 3)
    if lado == 0:
        return random.randint(margen, ANCHO - margen), margen
    if lado == 1:
        return ANCHO - margen, random.randint(margen, ALTO - margen)
    if lado == 2:
        return random.randint(margen, ANCHO - margen), ALTO - margen
    return margen, random.randint(margen, ALTO - margen)


def _choca_con(palabra, palabras):
    rect = palabra.rect()
    for otra in palabras:
        if rect.colliderect(otra.rect()) == True:
            return True
    return False


def iniciar_oleada(n, palabras):
    del palabras[:]

    if n <= 2:
        pool = POOL_FACIL
    elif n <= 4:
        pool = POOL_FACIL + POOL_MEDIA
    else:
        pool = POOL_MEDIA + POOL_DIFICIL

    cantidad = min(2 + n, 7)
    velocidad = min(18 + 10 * (n - 1), 90)

    usadas = set()
    for _ in range(cantidad):
        candidatos = []
        for t in pool:
            if t[0] not in usadas:
                candidatos.append(t)
        if not candidatos:
            break
        texto = random.choice(candidatos)
        usadas.add(texto[0])

        pos = _posicion_borde()
        prueba = PalabraObjetivo(texto, pos, velocidad)
        intentos = 0
        while intentos < 20 and _choca_con(prueba, palabras) == True:
            pos = _posicion_borde()
            prueba = PalabraObjetivo(texto, pos, velocidad)
            intentos = intentos + 1
        palabras.append(prueba)


class PalabraObjetivo:

    TAM_FUENTE_BASE = 36
    ESCALA_INICIAL = 2.2
    DURACION_ANIMACION = 350
    DURACION_FALLO = 500
    RADIO_TOQUE = 46

    COLOR_MARCO = (128, 0, 200)
    COLOR_VERDE = (0, 200, 0)
    COLOR_BLANCO = (255, 255, 255)
    COLOR_ROJO = (220, 30, 30)

    def __init__(self, texto, pos, velocidad):
        self.texto = texto
        self.font = pygame.font.Font(None, self.TAM_FUENTE_BASE)
        self.velocidad = velocidad

        self.balas_disparadas = 0
        self.impactos = 0
        self.destruida = False

        self.tiempo_animacion = 0
        self.tiempo_fallo = 0

        self.x, self.y = 0, 0
        self.poner_centro(pos[0], pos[1])

    def dimensiones(self):
        ancho = self.font.size(self.texto)[0] + 20
        alto = self.font.get_height() + 20
        return ancho, alto

    def centro(self):
        ancho, alto = self.dimensiones()
        return self.x + ancho / 2, self.y + alto / 2

    def poner_centro(self, cx, cy):
        ancho, alto = self.dimensiones()
        self.x = cx - ancho / 2
        self.y = cy - alto / 2

    def rect(self):
        ancho, alto = self.dimensiones()
        return pygame.Rect(self.x, self.y, ancho, alto)

    def avanzar(self, dt_ms, jugador_cx, jugador_cy):
        dist = self.velocidad * dt_ms / 1000.0
        px, py = self.centro()
        dx = jugador_cx - px
        dy = jugador_cy - py
        d = math.hypot(dx, dy)
        if d > dist:
            px = px + dx / d * dist
            py = py + dy / d * dist
        else:
            px, py = jugador_cx, jugador_cy
        self.poner_centro(px, py)
        return d <= self.RADIO_TOQUE

    def registrar_disparo(self):
        self.balas_disparadas = self.balas_disparadas + 1
        if self.balas_disparadas == 1:
            self.tiempo_animacion = self.DURACION_ANIMACION

    def recibir_impacto(self):
        if self.destruida == True:
            return False
        self.impactos = self.impactos + 1
        if self.impactos >= len(self.texto):
            self.destruida = True
            return True
        return False

    def actualizar(self, dt):
        if self.tiempo_animacion > 0:
            self.tiempo_animacion = max(0, self.tiempo_animacion - dt)
        if self.tiempo_fallo > 0:
            self.tiempo_fallo = max(0, self.tiempo_fallo - dt)

    def dibujar(self, screen):
        parte_verde = self.texto[:self.balas_disparadas]
        parte_blanca = self.texto[len(parte_verde):]

        factor_fallo = self.tiempo_fallo / self.DURACION_FALLO
        color_verde = lerp_color(self.COLOR_VERDE, self.COLOR_ROJO, factor_fallo)
        color_blanco = lerp_color(self.COLOR_BLANCO, self.COLOR_ROJO, factor_fallo)
        color_marco = lerp_color(self.COLOR_MARCO, self.COLOR_ROJO, factor_fallo)

        superficie_verde = self.font.render(parte_verde, True, color_verde)
        superficie_blanca = self.font.render(parte_blanca, True, color_blanco)

        padding = 10
        ancho_total = superficie_verde.get_width() + superficie_blanca.get_width()
        alto_total = self.font.get_height()
        marco_ancho = ancho_total + padding * 2
        marco_alto = alto_total + padding * 2

        marco_x = self.x
        marco_y = self.y

        marco = pygame.Rect(marco_x, marco_y, marco_ancho, marco_alto)
        pygame.draw.rect(screen, (0, 0, 0), marco)
        pygame.draw.rect(screen, color_marco, marco, 3)

        if self.tiempo_animacion > 0:
            factor_anim = self.tiempo_animacion / self.DURACION_ANIMACION
            borde = int(marco_alto / 2 + (marco_alto * self.ESCALA_INICIAL) * factor_anim)
            pop = marco.inflate(borde, borde)
            pygame.draw.rect(screen, color_marco, pop, max(1, int(4 * factor_anim)))

        screen.blit(superficie_verde, (marco_x + padding, marco_y + padding))
        screen.blit(superficie_blanca, (marco_x + padding + superficie_verde.get_width(), marco_y + padding))
