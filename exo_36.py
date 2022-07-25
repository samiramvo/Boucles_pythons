print("Entrz les longueurs des cotés du triangle:")
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
if x==y==z:
    print("Triangle équilatérale")
if x==y or x==z or y==z:
    print("Triangle isocèle")
if x!=y and x!=z and y!=z:
    print("Triangle scalène")