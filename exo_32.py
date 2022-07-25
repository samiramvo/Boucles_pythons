def ident (lettre):
    if lettre in('a','e','i','o','u'):
        return "{} est une voyelle"%format(lettre)
    else:
        return"{} est une consonne"%format(lettre)

print(ident('i'))
