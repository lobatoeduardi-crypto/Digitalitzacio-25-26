notas = {'Anna': [8, 9, 7], 'Pau': [5, 6, 6]}

for alumno, lista_notas in notas.items():
    media = sum(lista_notas) / len(lista_notas)
    print(f"{alumno} → {round(media, 2)}")
