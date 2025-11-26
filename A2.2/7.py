# Diccionario de notas
notes = {
    'Anna': [8, 9, 7],
    'Pau': [5, 6, 6]
}

for alumne, llista_notes in notes.items():
    mitjana = sum(llista_notes) / len(llista_notes)
    print(alumne, "→", round(mitjana, 2))
