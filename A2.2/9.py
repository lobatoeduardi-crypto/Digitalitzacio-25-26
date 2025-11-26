# Diccionario dentro de un diccionario
alumnes = {
    'Marta': {'edat': 18, 'nota_final': 8.5},
    'Joan': {'edat': 19, 'nota_final': 6.7},
    'Laura': {'edat': 20, 'nota_final': 9.1}
}

millor_alumne = ""
millor_nota = -1

for nom, dades in alumnes.items():
    if dades["nota_final"] > millor_nota:
        millor_nota = dades["nota_final"]
        millor_alumne = nom

print("L'alumne amb millor nota és:", millor_alumne)
