import tostadas_pipo.utilidades
print("1) import tostadas_pipo.utilidades -> OK")

from tostadas_pipo import utilidades
print("2) from tostadas_pipo import utilidades -> OK")

from tostadas_pipo.utilidades import *
print("3) from tostadas_pipo.utilidades import * -> OK")

from tostadas_pipo.utilidades import calculos
print("4) from tostadas_pipo.utilidades import calculos -> OK")
print("suma_total(10) =", calculos.suma_total(10))

from tostadas_pipo.utilidades.impuestos import impuesto_iva14
print("5) from tostadas_pipo.utilidades.impuestos import impuesto_iva14 -> OK")
print("impuesto_iva14(200) =", impuesto_iva14(200))
