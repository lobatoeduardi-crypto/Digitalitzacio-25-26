# Fusionar dos diccionarios
preus1 = {'pa': 1.2, 'llet': 0.9}
preus2 = {'formatge': 2.5, 'pa': 1.1}

fusionat = preus1.copy()
fusionat.update(preus2)   # Los valores de preus2 prevalecen

print(fusionat)
