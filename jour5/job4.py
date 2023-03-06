def plusGrand(liste):
    
    if len(liste) == 1:
        return liste[0]

    if liste[0] > liste[1]:
        liste[1] = liste[0]

    return plusGrand(liste[1:])

print(plusGrand([5, 23, 61, 17, 6]))