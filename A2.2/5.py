# Contar apariciones de letras
palabra = input("Introduce una palabra: ")
conteo = {}

for letra in palabra:
    conteo[letra] = conteo.get(letra, 0) + 1

print(conteo)
