#%%
#problema 1:
numero=float(input("Ingrese el monto depositado: "))
interes=0.04
año1 = numero * (1 + interes)
print("Año1:" + str(round(año1, 2)))
año2 = año1 * (1 + interes)
print("Año2:" + str(round(año2, 2)))
año3 = año2 * (1 + interes)
print("Año3:" + str(round(año3, 2)))

# %%
#problema 2:
print("ECUACIÓN CUADRÁTICA: aX² + bX + c = 0")
a = float(input("Escriba el valor de A: "))
b = float(input("Escriba el valor de B: "))
c = float(input("Escriba el valor de C: "))

if a == b == c == 0:
        print("Todos los números son solución.")
elif a == b == 0:
        print("La ecuación no tiene solución.")
elif a == 0:
        print(f"La ecuación tiene una solución: {- c / b}")
else:
        d = b * b - 4 * a * c
        if d < 0:
            print("La ecuación no tiene solución real.")
        elif d == 0:
            print(f"La ecuación tiene una solución: {- b / (2 * a)}")
        else:
            print(
                f"La ecuación tiene dos soluciones: {(-b - d ** 0.5) / (2 * a)} y {(-b + d ** 0.5) / (2 * a)}"
            )

