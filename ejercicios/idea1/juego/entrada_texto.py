"""Entrada de texto del jugador (mecanografia).

Mantiene el texto escrito y la palabra enemiga activa. Usa variables de
modulo: texto_actual y palabra_activa.

El matching ignora mayusculas/minusculas (Caps Lock no rompe el juego).

Uso tipico dentro del bucle:
    entrada_texto.actualizar_texto(eventos, palabras)
"""
import pygame

from juego import sonidos


texto_actual = ""
palabra_activa = None


def reiniciar():
    global texto_actual
    global palabra_activa
    texto_actual = ""
    palabra_activa = None


def actualizar_texto(eventos, palabras):
    global texto_actual
    global palabra_activa

    for evento in eventos:
        if evento.type == pygame.TEXTINPUT:
            for caracter in evento.text:
                caracter = caracter.lower()
                if texto_actual == "":
                    for palabra in palabras:
                        if palabra.texto.startswith(caracter):
                            palabra_activa = palabra
                            texto_actual = caracter
                            break
                elif len(texto_actual) < len(palabra_activa.texto):
                    if caracter == palabra_activa.texto[len(texto_actual)]:
                        texto_actual = texto_actual + caracter
                    else:
                        palabra_activa.tiempo_fallo = palabra_activa.DURACION_FALLO
                        texto_actual = ""
                        palabra_activa = None
                        sonidos.reproducir("tecla_errada")
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_actual = texto_actual[:-1]
                if texto_actual == "":
                    palabra_activa = None

    return texto_actual
