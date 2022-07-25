liste=[]
for i in range(100,401):
    j=str(i)
    if(int(j[0]%2==0) and int(j[1]%2==0) and int(j[2]%2==0)):
        liste.append(j)

print(",".join(liste))