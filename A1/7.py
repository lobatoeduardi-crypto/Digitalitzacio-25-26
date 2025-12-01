contador=0
palabra="programacion"
letra="a"

for x in palabra:
    if x == letra:
        contador+=1

        print("A la palabra ", palabra, "hay ", contador, "letras", letra)