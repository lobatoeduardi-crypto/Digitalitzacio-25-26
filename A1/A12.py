texto1 = "Hello World"
texto2 = "Hola mon!!!"

coincidencias = 0
for i in range(min(len(texto1), len(texto2))):
    if texto1[i] == texto2[i]:
        coincidencias += 1

print("Caracteres iguales en la misma posición:", coincidencias)
