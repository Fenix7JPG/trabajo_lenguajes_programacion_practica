"""Balas del jugador: una por cada caracter correcto escrito.

Al escribir un caracter correcto, main llama disparar() con la palabra activa
como objetivo. La bala viaja hasta la palabra y le quita un impacto; la
palabra muere cuando sus impactos alcanzan la cantidad de letras.

Uso en el bucle:
    balas.disparar((x, y), palabra_activa)
    destruidas = balas.avanzar(dt)
    balas.dibujar(screen)
    balas.reiniciar()   # al reiniciar partida o pasar de oleada
"""
import math

import pygame


class Bala:

    RADIO = 3
    VELOCIDAD = 520.0
    COLOR = (255, 220, 80)

    def __init__(self, x, y, objetivo):
        self.x = x
        self.y = y
        self.objetivo = objetivo

    def avanzar(self, dt_ms):
        if self.objetivo.destruida == True:
            return True
        cx, cy = self.objetivo.centro()
        dist = self.VELOCIDAD * dt_ms / 1000.0
        dx = cx - self.x
        dy = cy - self.y
        d = math.hypot(dx, dy)
        if d <= dist:
            self.x = cx
            self.y = cy
            return True
        self.x = self.x + dx / d * dist
        self.y = self.y + dy / d * dist
        return False

    def dibujar(self, screen):
        pygame.draw.circle(screen, self.COLOR, (int(self.x), int(self.y)), self.RADIO)


_balas = []


def disparar(origen, objetivo):
    objetivo.registrar_disparo()
    _balas.append(Bala(origen[0], origen[1], objetivo))


def avanzar(dt_ms):
    destruidas = []
    for bala in list(_balas):
        if bala.avanzar(dt_ms) == True:
            _balas.remove(bala)
            if bala.objetivo.destruida == True:
                continue
            if bala.objetivo.recibir_impacto() == True:
                destruidas.append(bala.objetivo)
    return destruidas


def dibujar(screen):
    for bala in _balas:
        bala.dibujar(screen)


def reiniciar():
    del _balas[:]
