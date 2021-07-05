#%%
#1
nombres=[]
notas=[]
n = int(input("Ingrese la cantidad de alumnos: "))
for x in range(n):
    nom=input("Ingrese el nombre del alumno:")
    nombres.append(nom)
    no1=int(input("Ingrese la primera nota:"))
    no2=int(input("Ingrese la segunda nota:"))
    no3=int(input("Ingrese la tercera nota:"))
    notas.append([no1,no2,no3])
for x in range(n):
    print(nombres[x],notas[x][0],notas[x][1],notas[x][2])
#%%
#2
aplazados = aprobados = 0
prom=[]
for x in range(n):
    total=(notas[x][0]+notas[x][1]+notas[x][2])/3
    prom.append(total)
    print(nombres[x], prom[x])
    while True:
        if prom[x] == 0:
            break
 
        if prom[x] > 10:
            continue
        else:
            if prom[x] < 4:
                aplazados += 1
            elif prom[x] >= 4 and prom <=10:
                aprobados += 1
print('\nNumero de aprobados %d' %aprobados)
print('Numero de aplazados %d' %aplazados)

# %%
#3
total=0
for x in range(n):
    total=prom[x]/n
for x in range(n):
    print(total)
#%%
#4
may=0
mayor=prom[0]
men=0
menor=prom[0]

for x in range(1,n):
    if prom[x]>mayor:
        mayor=prom[x]
        may=x
for x in range(1,n):
    if prom[x]<menor:
        menor=prom[x]
        men=x
print("Alumno con mayor promedio")
print(nombres[may])
print("con un promedio de",mayor)
print("Alumno con menor promedio")
print(nombres[men])
print("con un promedio de",menor)
#%%

