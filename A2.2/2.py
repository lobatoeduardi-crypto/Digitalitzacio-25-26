# Añadir y eliminar elementos
cotxe = {
    "marca": "Toyota",
    "model": "Corolla",
    "any": 2018
}

cotxe["color"] = "rojo"   # Añadir clave
del cotxe["any"]          # Eliminar clave

print(cotxe)