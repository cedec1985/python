tags=['vacances','italie','juillet',None]
nom_fichier='_'.join(filter(None,tags))#filtrer sans None
print(nom_fichier)
nom_fichier='_'.join([i for i in tags if i])
print(nom_fichier)