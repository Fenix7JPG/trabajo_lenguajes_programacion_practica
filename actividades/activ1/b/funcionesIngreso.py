def es_numero(valor):
    if isinstance(valor, bool):
        print("Error:", valor, "no es un número válido")
        return False
    
    if not isinstance(valor, (str, int, float)):
        print("Error:", valor, "no es un número válido")
        return False
    
    if isinstance(valor, (int, float)):
        valor_str = str(valor)
    else:
        valor_str = valor
    
    if len(valor_str) == 0:
        print("Error: string vacío no es un número válido")
        return False
    
    for caracter in valor_str:
        if caracter not in "0123456789":
            print("Error:", caracter, "no es un dígito válido (0-9)")
            return False
    
    return True