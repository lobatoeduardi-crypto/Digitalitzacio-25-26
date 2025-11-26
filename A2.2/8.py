# Filtrar por valor
preus = {'motxilla': 45, 'llapis': 1, 'calculadora': 25}

preus_filtrats = {}

for producte, preu in preus.items():
    if preu > 20:
        preus_filtrats[producte] = preu

print(preus_filtrats)
