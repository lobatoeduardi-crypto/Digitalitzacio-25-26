# Diccionario de alumnos
alumnes = {
    'Marta': {'edat': 18, 'nota_final': 8.5},
    'Joan': {'edat': 19, 'nota_final': 6.7}
}

# Encontrar alumno con mejor nota
millor_alumne = max(alumnes, key=lambda x: alumnes[x]['nota_final'])
print(f"El alumno con mejor nota es {millor_alumne}")

