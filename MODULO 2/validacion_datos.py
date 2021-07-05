
def solicitar_entero( mensaje = "Introduce un número entero: " ):
    try:
        n = int(input(mensaje))
        return n
        # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número")
        solicitar_entero(mensaje)

def solicitar_float( mensaje = "Introduce un número decimal: " ):
    try:
        n = float(input(mensaje))
        return n
        # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número")
        solicitar_float(mensaje)