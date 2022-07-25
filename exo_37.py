mont=input("Entrez le mois:")
jours=int(input("Entrez le nombre d jours:"))

if mont in ('Janvier','Février','Mars'):
    season='winter'
elif mont in ('Avril','Mai','Juin'):
    season='spring'
elif mont in ('Juillet','Aout','Septembre'):
    season='summer'
else:
    season='autumn'

if (mont=='Mars') and(jours>19):
    season='springs'
if (mont=='June') and(jours>20):
    season='summer'

if (mont=='Septembre') and(jours>21):
    season='autumn'
if (mont=='December') and(jours>20):
    season='winter'

print("Season is ",season)
