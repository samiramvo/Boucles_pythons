jours=int(input("Entrez le nombre de jours:"))
mont=input("Entrez le mois:")
if mont =='Décembre':
    astro='Sagittaire' if (jours<22) else 'Capricone'
elif mont=='Janvier':
    astro='Capricone' if (jours<20) else 'Verseau'
elif mont=='Février':
    astro='Verseau' if (jours<19) else 'Poisson'
elif mont=='Mars':
    astro='Verseau' if (jours<21) else 'aries'
    
elif mont=='Avril':
    astro='Aries' if (jours<20) else 'Taureau'
elif mont=='Mai':
    astro='Taureau' if (jours<21) else 'Gémeaux'
elif mont=='Juin':
    astro='Gémeaux' if (jours<21) else 'Cancer'
elif mont=='Juillet':
    astro='Cancer' if (jours<23) else 'leo'
elif mont=='Aout':
    astro='leo' if (jours<23) else 'Virgo'
elif mont=='Septembre':
    astro='Virgo' if (jours<23) else 'libra'
elif mont=='Octobre':
    astro='libra' if (jours<23) else 'scorpio'
elif mont=='Novembre':
    astro='scorpio' if (jours<22) else 'Sagittaire'

print("Signe astrologique:",astro)
    
    