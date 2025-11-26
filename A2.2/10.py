# Frecuencia de palabras en una frase

frase = input("Introduce una frase: ")

palabras = frase.split()
frecuencia = {}

for palabra in palabras:
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print(frecuencia)
