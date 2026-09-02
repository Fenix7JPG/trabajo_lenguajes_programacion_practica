"""Modulo de sonido: carga los .wav de assets/sonidos y los reproduce.

Uso:
    sonidos.cargar()                    # una vez, despues de pygame.init()
    sonidos.reproducir("tecla_errada")  # no hace nada si no cargo

Sonidos disponibles:
    explosion_enemigo, explosion_jugador, tecla_errada
"""
import os

import pygame

_CARPETA = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", "assets", "sonidos"))

NOMBRES = ["explosion_enemigo", "explosion_jugador", "tecla_errada"]

_sonidos = {}


def cargar():
    for nombre in NOMBRES:
        ruta = os.path.join(_CARPETA, nombre + ".wav")
        if os.path.exists(ruta):
            try:
                _sonidos[nombre] = pygame.mixer.Sound(ruta)
            except pygame.error:
                pass


def reproducir(nombre):
    if nombre in _sonidos:
        _sonidos[nombre].play()
