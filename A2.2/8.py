# Diccionario de precios
preus = {'motxilla': 45, 'llapis': 1, 'calculadora': 25}

# Filtrar productos > 20 €
preus_filtrats = {producte: preu for producte, preu in preus.items() if preu > 20}

print(preus_filtrats)

