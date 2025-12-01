# Invertir una lista

list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
lista_invertida = []

# Recorremos la lista desde el final hacia el inicio
for i in range(len(list_num)-1, -1, -1):
    lista_invertida.append(list_num[i])

print("Lista original:", list_num)
print("Lista invertida:", lista_invertida)