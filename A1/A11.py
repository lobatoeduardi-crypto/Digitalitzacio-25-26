texto = "atggatcatttta"

letra = 'a'
contador = 0

for i in range(len(texto)):
    if texto[i] == letra:
        print(f"Posición: {i}")
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces.")