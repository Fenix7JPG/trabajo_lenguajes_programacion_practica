import sys

ruta_proyecto = "D:/Proy_Github/lenguajes_programacion/actividades/activ1"

sys.path.append(ruta_proyecto + "/a")
sys.path.append(ruta_proyecto + "/b")

from funcionesComparacion import maximo, minimo, son_iguales, son_diferentes
from funcionesIngreso import es_numero

print("Ruta absoluta del proyecto:", ruta_proyecto)
print("Maximo entre 12 y 7:", maximo(12, 7))
print("Minimo entre 12 y 7:", minimo(12, 7))
print("¿12 y 12 son iguales?:", son_iguales(12, 12))
print("¿12 y 7 son diferentes?:", son_diferentes(12, 7))
print("¿El texto 456 es numero?:", es_numero("456"))
print("¿El texto 4a6 es numero?:", es_numero("4a6"))
