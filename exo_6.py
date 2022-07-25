def comp(nombre):
    som=0
    some=0
    for i in nombre :
        if i%2==0:
            som+=1

        return "Nombre de nombres pairs",som
        if i%2==1:
            some+=1
        return "Nombre de nombres impairs",some

print(comp((1,2,3,4,5,6,7,8,9)))
    