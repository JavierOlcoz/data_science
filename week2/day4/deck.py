"""Lo he probado y se me ejecuta solo con el comando "python deck.py"
"""

acum = 0
deck = []
while acum < 4:
    acum2 = 0
    if acum == 0:
        z = (" Corazones")
        while acum2 < 10:
            y = str(acum2 + 1) + z
            deck.append(y)
            acum2 += 1
    elif acum == 1:
        z = (" Picas")
        while acum2 < 10:
            y = str(acum2 + 1) + z
            deck.append(y)
            acum2 += 1
    elif acum == 2:
        z = (" Tréboles")
        while acum2 < 10:
            y = str(acum2 + 1) + z
            deck.append(y)
            acum2 += 1
    else: 
        z = (" Rombos")
        while acum2 < 10:
            y = str(acum2 + 1) + z
            deck.append(y)
            acum2 += 1
    acum += 1



print(deck)

