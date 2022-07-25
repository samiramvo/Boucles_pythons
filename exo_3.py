import random

print("Deviner un nombre entre 1 et 9")
a,b=random.randint(1,10),0
while a!=b:
    b=int(input("Entrez un nombre compris entre 1 et 10:"))

print("Bien Joué")