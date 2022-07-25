age=int(input("Entrez l'année du chien en année humaine: "))

age_rest=age-2
if age>2:
    age_hum=age_rest*4+(2*10.5)
    print(age_hum)
if age>0 and age<=2:
    age_hum=age*10.5
    print(age_hum)
