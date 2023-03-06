def longueur(chaine):
    if chaine == '':
        return 0
    return 1 + longueur(chaine[1:])

print(longueur("plein"))