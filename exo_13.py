liste=[]

numb=[x for x in input().split(',')]

for ent in numb:
    x=int(ent,2)
    if not x%5:
        liste.append(ent)

print(','.join(liste))