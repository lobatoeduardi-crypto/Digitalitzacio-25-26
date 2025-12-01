# Pedir frase
frase = input("Introduce una frase: ")

# Separar en palabras
paraules = frase.split()

# Contar frecuencia de palabras
frequencia = {}
for paraula in paraules:
    frequencia[paraula] = frequencia.get(paraula, 0) + 1

print(frequencia)

