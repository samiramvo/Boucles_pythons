from numpy import sometrue


print("Entrez une chaine de caractére:")
chaine=input()
som=some=0
for i in chaine:
        if i.isdigit():
            som+=1
        
        elif i.isalpha():
            some+=1
        
        else:
            pass

print("Letters:",some)
print("Chiffre",som)