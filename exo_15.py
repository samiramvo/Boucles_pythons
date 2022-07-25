import re
mot=input("Entrez le mot de passe:")
while True:
    if len(mot)<6 or len(mot)>16:
        break
    elif not re.search("[a-z]",mot): 
        break
    elif not re.search("[0-9]",mot):
        break
    elif not re.search("[A-Z]",mot):
        break
    elif not re.search("[$#@]",mot):
        break
    elif not re.search("\s",mot):
        break
    else:
        print("Valid password")
        x=False
        break
