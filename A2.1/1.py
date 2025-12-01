# 1. Crear y mostrar una lista
l = [10, 20, 30, 40, 50]
print(l)

# Añadir un elemento
l.append(60)
print(l)

# Acceder a un elemento por posición
print(l[4])  # ejemplo, 5º elemento

# 2. Lista de nombres, mostrar primero y último
nombres = ["Ana", "Luis", "María", "Carlos", "Sofía"]
print("Primer nombre:", nombres[0])
print("Último nombre:", nombres[-1])

# 3. Añadir y eliminar elementos
nombres.append("Pedro")   # añadir al final
print(nombres)

eliminado = nombres.pop(0)  # eliminar primero
print("Eliminado:", eliminado)
print(nombres)

# 4. Mostrar longitud de las listas
print("Longitud de l:", len(l))
print("Longitud de nombres:", len(nombres))