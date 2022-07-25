
print("Entrez le nombre des entiers:")
ent=int(input())
sum=0
for i in range(ent):
    a=int(input())
sum+=a

print("Somme:{},Moyenne:{}" %format(sum,sum/ent))