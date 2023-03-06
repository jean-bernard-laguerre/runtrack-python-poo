def puissance(x, n):
    if n == 1:
        return x
    return x * puissance(x, n-1)

print(puissance(4,2))