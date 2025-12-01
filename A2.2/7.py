# Diccionario de notas
notes = {'Anna': [8, 9, 7], 'Pau': [5, 6, 6]}

# Calcular y mostrar medias
for alumne, llistanotes in notes.items():
    mitjana = sum(llistanotes) / len(llistanotes)
    print(f"{alumne} → {mitjana:.2f}")

