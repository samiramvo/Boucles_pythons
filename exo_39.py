annee=int(input("Entrez l'année:"))
if (annee - 2000)%12 ==0:
    signe='Dragon'
if (annee - 2000)%12 ==1:
    signe='Snake'
if (annee - 2000)%12 ==2:
    signe='Horse'
if (annee - 2000)%12 ==3:
    signe='sheep'
if (annee - 2000)%12 ==4:
    signe='Monkey'
if (annee - 2000)%12 ==5:
    signe='Rooster'
if (annee - 2000)%12 ==6:
    signe='Dog'
if (annee - 2000)%12 ==7:
    signe='Pig'
if (annee - 2000)%12 ==8:
    signe='Rat'
if (annee - 2000)%12 ==9:
    signe='Ox'
if (annee - 2000)%12 ==10:
    signe='Tiger'
else:
    signe='Hare'
print("Ton signe de zodiaque est :",signe)