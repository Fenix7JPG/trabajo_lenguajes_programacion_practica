"""Entrada de texto del jugador (mecanografia).

Mantiene el texto escrito y la palabra enemiga activa. Usa variables de
modulo: texto_actual y palabra_activa.

Robustez:
- El matching ignora mayusculas/minusculas (Caps Lock no rompe el juego).
- Si una utilidad de teclado genera el mismo caracter dos veces en el mismo
  fotograma, se colapsa a uno (si no, la 2a copia resetearia el progreso).

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


def _caracteres_del_lote(eventos):
    """Caracteres de TEXTINPUT del lote, sin duplicados consecutivos.

    Un tecleo fisico normal nunca produce la misma letra dos veces dentro de
    un mismo fotograma (16 ms); si llega duplicada es doble registro de la
    MISMA tecla y se cuenta una sola vez.
    """
    caracteres = []
    for evento in eventos:
        if evento.type == pygame.TEXTINPUT:
            for caracter in evento.text:
                if len(caracteres) > 0 and caracteres[-1] == caracter:
                    continue
                caracteres.append(caracter)
    return caracteres


def actualizar_texto(eventos, palabras):
    global texto_actual
    global palabra_activa

    for caracter in _caracteres_del_lote(eventos):
        caracter = caracter.lower()
        if caracter == "":
            continue
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

    for evento in eventos:
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_actual = texto_actual[:-1]
                if texto_actual == "":
                    palabra_activa = None

    return texto_actual
