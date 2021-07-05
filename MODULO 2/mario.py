
import validacion_datos as v

def mostrar_triangulo(h):

    for i in range(1,h+1):
        print(" " * (h-i) + "#" * i)  

if __name__ == "__main__":
    h = v.solicitar_entero("Ingrese altura del triangulo entre 1 y 8: ")
while  h <9:
    if h >0 :
        mostrar_triangulo(h)
        break
    else:
     h = v.solicitar_entero("Ingrese altura del triangulo entre 1 y 8: ")   
if h >= 9:
    h = v.solicitar_entero("Ingrese altura del triangulo entre 1 y 8: ")
    
# %%
