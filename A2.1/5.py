# Lista con elementos repetidos
list_num = [6, 9, 6, 9]
print("Lista original:", list_num)

# Crear una nueva lista sin duplicados
lista_sin_duplicados = []

for i in range(len(list_num)):
    if list_num[i] not in lista_sin_duplicados:
        lista_sin_duplicados.append(list_num[i])

print("Lista sin duplicados:", lista_sin_duplicados)