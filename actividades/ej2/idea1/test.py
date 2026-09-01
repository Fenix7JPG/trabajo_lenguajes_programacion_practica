import pygame
import math
import random


ANCHO = 960
ALTO = 540

texto_actual = ""
palabra_activa = None
puntos = 0
oleada = 1
game_over = False


POOL_FACIL = ["sol", "luz", "mar", "pan", "red", "ojo", "pez", "tio"]
POOL_MEDIA = ["árbol", "nieve", "queso", "playa", "monte",
              "viento", "nube", "río", "flor", "azul"]
POOL_DIFICIL = ["canción", "corazón", "azúcar", "teléfono", "murciélago",
                "avión", "camión", "lección", "música", "número",
                "rápido", "difícil", "búho", "día"]


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


def _choca_con(palabra, palabras):
    rect = palabra.rect()
    for otra in palabras:
        if rect.colliderect(otra.rect()) == True:
            return True
    return False


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


def actualizar_texto(eventos, palabras):
    global texto_actual
    global palabra_activa

    for evento in eventos:
        if evento.type == pygame.TEXTINPUT:
            for caracter in evento.text:
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
                        palabra_activa.tiempo_fallo = PalabraObjetivo.DURACION_FALLO
                        texto_actual = ""
                        palabra_activa = None
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_BACKSPACE:
                texto_actual = texto_actual[:-1]
                if texto_actual == "":
                    palabra_activa = None

    return texto_actual


def lerp_color(color_a, color_b, factor):
    factor = max(0.0, min(1.0, factor))
    return tuple(int(a + (b - a) * factor) for a, b in zip(color_a, color_b))


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
        self.completado_valido = ""

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

    def definir_completado(self, nuevo_completado):
        if self.texto.startswith(nuevo_completado):
            if len(self.completado_valido) == 0 and len(nuevo_completado) > 0:
                self.tiempo_animacion = self.DURACION_ANIMACION
            self.completado_valido = nuevo_completado

    def actualizar(self, dt):
        if self.tiempo_animacion > 0:
            self.tiempo_animacion = max(0, self.tiempo_animacion - dt)
        if self.tiempo_fallo > 0:
            self.tiempo_fallo = max(0, self.tiempo_fallo - dt)

    def dibujar(self, screen):
        parte_verde = self.completado_valido
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


def main():
    global puntos
    global texto_actual
    global palabra_activa
    global oleada
    global game_over

    pygame.init()
    screen = pygame.display.set_mode((ANCHO, ALTO))
    clock = pygame.time.Clock()

    pygame.key.set_repeat(500, 50)

    fuente_hud = pygame.font.Font(None, 34)
    fuente_final = pygame.font.Font(None, 60)

    jugador_cx = ANCHO / 2
    jugador_cy = ALTO / 2
    jugador_radio = 22

    palabras = []
    oleada = 1
    iniciar_oleada(oleada, palabras)

    activo = True
    while activo:
        dt = clock.tick(60)

        eventos = pygame.event.get()

        for evento in eventos:
            if evento.type == pygame.QUIT:
                activo = False
            elif evento.type == pygame.KEYDOWN and game_over:
                if evento.key == pygame.K_r or evento.key == pygame.K_RETURN:
                    puntos = 0
                    oleada = 1
                    game_over = False
                    texto_actual = ""
                    palabra_activa = None
                    iniciar_oleada(oleada, palabras)
                elif evento.key == pygame.K_ESCAPE:
                    activo = False

        if not game_over:
            texto = actualizar_texto(eventos, palabras)

            for palabra in palabras:
                completado = texto if palabra is palabra_activa else ""
                palabra.definir_completado(completado)
                palabra.actualizar(dt)

            if palabra_activa is not None and texto == palabra_activa.texto:
                palabras.remove(palabra_activa)
                puntos = puntos + 1
                texto_actual = ""
                palabra_activa = None

            for palabra in list(palabras):
                if palabra.avanzar(dt, jugador_cx, jugador_cy):
                    game_over = True
                    texto_actual = ""
                    palabra_activa = None
                    break

            if not palabras:
                oleada = oleada + 1
                iniciar_oleada(oleada, palabras)

        screen.fill((30, 30, 30))

        for palabra in palabras:
            palabra.dibujar(screen)

        pygame.draw.circle(screen, (220, 30, 30), (int(jugador_cx), int(jugador_cy)), jugador_radio)
        pygame.draw.circle(screen, (255, 120, 120), (int(jugador_cx), int(jugador_cy)), jugador_radio, 2)

        hud = fuente_hud.render("Oleada " + str(oleada) + "   Puntos: " + str(puntos), True, (255, 255, 255))
        screen.blit(hud, (16, 12))

        if game_over:
            velo = pygame.Surface((ANCHO, ALTO), pygame.SRCALPHA)
            velo.fill((0, 0, 0, 160))
            screen.blit(velo, (0, 0))

            msg1 = fuente_final.render("PERDISTE", True, (220, 30, 30))
            msg2 = fuente_hud.render("Puntos: " + str(puntos) + "   Oleada: " + str(oleada), True, (255, 255, 255))
            msg3 = fuente_hud.render("R o Enter para reiniciar - ESC para salir", True, (200, 200, 200))
            screen.blit(msg1, msg1.get_rect(center=(ANCHO / 2, ALTO / 2 - 50)))
            screen.blit(msg2, msg2.get_rect(center=(ANCHO / 2, ALTO / 2 + 10)))
            screen.blit(msg3, msg3.get_rect(center=(ANCHO / 2, ALTO / 2 + 50)))

        pygame.display.flip()

    pygame.quit()


main()