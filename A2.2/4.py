# Comprobar existencia de una clave
capital_pais = {
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma"
}

pais = input("Introduce un país: ")

if pais in capital_pais:
    print("La capital de", pais, "es", capital_pais[pais])
else:

    print("Ese país no está en el diccionario.")