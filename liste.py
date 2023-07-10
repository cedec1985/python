liste=range(10)
index=9
print(liste[index])
try:
    r=liste[index]
    print(r)
except IndexError:
    print("l'index {} n'existe pas.".format(index))
r=liste[index] if len(liste) > index else None # à conseiller

prenom=['pierre','alain','marie'] #comment enlever un élément d'une liste
prenom_sans_p=[p for p in prenom if p!='pierre']
print(prenom_sans_p)