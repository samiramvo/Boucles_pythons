
def tempC(temperature):
    C=(5*(temperature-32))/9
    return C
def tempF(temperature):
    F=((9*temperature)/5)+32
    return F


print("Veuillez tapez une option:")
print("Tapez 1 pour convertir farenheit en celsuis")
print("Tapez 2 pour convertir celsuis en farenheit")
print("Entrez l'option:")
numb=int(input())

if numb==1:
    print("Veuillez entrez la temperature:")
    temp=int(input())
    print(tempC(temp),"°C")

if numb==2:
    print("Veuillez entrez la temperature:")
    temp=int(input())
    print(tempF(temp),"°F")