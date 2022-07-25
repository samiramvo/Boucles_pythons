mont=str(input("Entrez un mois:"))
if mont=="Février":
    print("Nombre de jours: 28 ou 29")
if mont in("Juin","Septembre","Avril"):
    print("Nombre de jours: 30")
if mont in ("Janvier","Mars","Mai","Juillet","Aout","Octobre","Novembre","Decembre"):
    print("Nombre de jours: 31")