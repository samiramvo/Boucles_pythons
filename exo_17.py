lig=int(input("Entrez le nombre de lignes:"))
for i in range(1,lig+1):
    for j in range(1,6):
        if (j==1 or j==5) and i!=1:
            print("*",end="")
        elif(i==1 or i==(lig+1)//2) and(j>1 and j<5):
             print("*",end="")
        else:
            print("",end="")

    print()
