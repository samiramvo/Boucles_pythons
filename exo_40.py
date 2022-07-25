a=int(input("Entrez le premier chiffre:"))
b=int(input("Entrez le deuxième chiffre:"))
c=int(input("Entrez le troisième chiffre:"))
if a>b:
    if a<c:
        median=a
    elif b>c:
        median=b
    else:
        median=c
else:
    if a>c:
        median=a
    elif b<c:
        median=b
    else:
        median=c

print("La médiane est de:",median)