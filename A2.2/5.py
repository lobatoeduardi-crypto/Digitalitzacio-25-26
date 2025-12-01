# Pedir palabra
palabra = input("Introduce una palabra: ")

# Contar apariciones de letras
frecuencia = {}
for letra in palabra:
    frecuencia[letra] = frecuencia.get(letra, 0) + 1

print(frecuencia)

