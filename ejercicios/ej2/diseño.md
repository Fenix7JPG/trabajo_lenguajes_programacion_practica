# Ej 2 - Mecanografia espacial

Juego de mecanografia con pygame: un punto azul (el jugador) en el centro
y palabras-enemigo que se acercan desde los bordes. Destruyes una palabra
escribiendola completa.

## Mecanicas

- El primer caracter correcto activa una palabra; cada caracter correcto
  dispara una bala (la letra viaja hasta la palabra).
- Cada bala que llega causa un impacto; la palabra muere al recibir un
  impacto por cada letra (su marco crece y desaparece).
- Una letra errada borra tu progreso en esa palabra.
- Si un enemigo toca al jugador, pierdes: Enter reinicia, ESC sale.
- Cada oleada suma cantidad de enemigos (hasta 7), velocidad y largo de
  palabra (hasta 5).

## Configuración del entorno

    py -3.12 -m venv .venv
    .venv\Scripts\activate
    pip install pygame

## Ejecutar

    python main.py

## Estructura

    main.py                 estado del juego y bucle principal
    juego/constantes.py     valores: ventana, colores, jugador, palabras
    juego/palabras.py       enemigos (PalabraObjetivo) y oleadas
    juego/entrada_texto.py  interpreta las teclas escritas
    juego/balas.py          balas-caracter y sus impactos
    juego/visual.py         dibujo de todo lo que se ve en pantalla
