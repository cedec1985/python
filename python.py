import time
from typing import List
import random
import os
import sys


liste=[1,2,3]
print(id(liste))
liste.append(4)
print(id(liste))
list="pierre"
print(id(list))
list +="dupont"
print(id(list))
lisst=range(99999)
a=time.time()
resultat=''
for number in lisst:
    resultat += str(number)
print(resultat)
b=time.time()
print("temps d'exécution: {}".format(b-a))
c=time.time()
resultat: List[str]=[]
for number in lisst:
    resultat.append(str(number))
resultat_final=''.join(resultat)
d=time.time()
print("temps d'exécution:{}".format(d-c))
dc=[]
dc.append(['orange'])
dc.append(['apples'])
print("la liste des fuits:",dc)
print(len(dc))
print(dc)

liste=['bonjour', 'tout','le','monde']
for i, mot in enumerate(liste):
    if i>=0:
        print(mot)

def multiplication(a,b):
    return a*b
multiplication = lambda a, b:a*b
resultat = multiplication(5,10)
print(resultat)

def print_bonjour():
    print('bonjour')
print_bonjour()
print_bonjour=lambda:print('bonjour')
print_bonjour()

print_mot=lambda m:print(m)
print_mot('python')

utilisateurs=[('user1','etienne'),
              ('user4','arnaud'),
              ('user3','camille'),
              ('user5','bernard')]
utilisateurs.sort(key=lambda x:x[0])
print(utilisateurs)

for m in[1,2,3,4,5]:
    print(m)
for l in 'udemy':
    print(l)
for key in {'user 1':'paul','user 2':'pierre'} :
    print(key)
iterateur=iter('udemy')
print(iterateur)
print(next(iterateur))
print(next(iterateur))

liste =[1,2,3,4,5,6]
liste =[i*2 for i in liste]
print(liste)

liste=[1,2,3,4,5,6,7,8]
liste=[i*2 for i in liste if i%2 ==0]
print(liste)

liste=[1,2,3,4,5,6,7,8]
liste=[i*2 if i%2 ==0 else i*3 for i in liste ]
print(liste)
def exemple_generateur():
    yield 1
    yield 2
    yield 3
generateur=exemple_generateur()
print(type(generateur))
print(next(generateur))
print(next(generateur))

def custom_range(n):
    for i in range(1,n+1):
        yield i
a=custom_range(11)
print(type(a))
print(next(a))
print(next(a))
# ici
class custom_range:
    def __init__(self,maximum):
        self.i =0
        self.max=maximum
    def __iter__(self):
        return self
    def __next__(self):
        if self.i <self.max:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()
a=custom_range(15)
print(next(a))
for i in a:
    print(i)

a={'pierre':'18','alfred':'20'}
print(type(a))
for i,int in enumerate(a):
    if i>=1:
        print(int)

from random import randint
class lettre_random:
    def __init__(self,nom_r):
        self.i =0
        self.max=len(nom_r)
        self.nom_r=[]
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < self.max:
            lettre=self.nom_r.pop(randint(0,len(self.nom_r)-1))
            self.i +=1
            return lettre
        else:
            raise StopIteration()
nom_r=('bonjour')
nom_random=lettre_random(nom_r)
nom_melange=[l for l in nom_r]
print(nom_melange)
print(''.join(nom_melange))

import sys
print(sys.path)
print(sys.platform)
print(sys.version)
print(sys.executable)
print(sys.argv)
print(sys.getwindowsversion())

from pprint import pprint
pprint(dir)
pprint(dir(os))
os.system('echo bonjour')
pprint(dir([]))
print([].append.__doc__)
pprint(type(pprint))
age=[5,12,15,20,17]
autorisation=any(a>=18 for a in age)
print(autorisation)
autorisation=all(a>=18 for a in age)
print(autorisation)
exemple=any([False,False,True,False])
exemple=any([False,False,False,False])
exemple_1=all([True,True,True,True])
exemple_1=all([True,False,True,True])

def addition(*args):
    return(sum(args))
print(addition(5,2,6,10))
def invites(invite_vip,*args):
    print ('{}est un vip'.format(invite_vip))
    for invite in args:
        print('{} est un invite normal'.format(invite))
invites('paul','pierre','marie','max')
def invitées(invite_vip,*args,**kwargs):
    print('{} est un vip'.format(invite_vip))
    for invite in args:
        print('{} est un invité normal'.format(invite))
    indesirables=kwargs.get('indesirable')
    if indesirables:
        print('ces invites sont indesirables:{}'.format(','.join(indesirables)))
invitées('paul','pierre','marie','max',indesirable=['simon','jean','julie'])

a={5,6,8,9}
b={5,6,10,12}
print(a.union(b))
print(a|b)
print(a-b)
print(b-a)
print(a&b)
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a^b)
import random
print(random.__doc__)#docstrings
print(random.randint.__doc__)
def multiplication(a,b):
    """multiplie deux nombres et retourne le résultat de l'opération
    :param a:le premier nombre
    :param b:le second nombre
    :type a:int
    :type b:int
    :return:le résultat de la multiplication
    :rtype:int

    :Example:

    >>>multiplication(2,5)
    10

    """
import re
print('\tbonjour')
print(r'\tbonjour')
a=re.match(r'','pierre dupont')
print(a)
a=re.match(r'(\w+)(\s)(\w+)','pierre dupont')
print(a.group(0))
print(a.group(2))
a=re.match(r'(?P<prenom>\w+) (?P<nom>\w+)','pierre dupont')
print(a.group('prenom'))
print(a.groups)
print(a.groupdict())
a=re.match(r'.+','pierre dupont')
print(a.group())
a=re.search(r' \+ ','pierre dupont + paul martin')
print(a.group())
text='item1 | item2 - item3 - item4 | item5'
a=re.split(r'\| | -',text)
print(a)
#récupérer une clé inexistante d'un dictionnaire
dic= {'pierre':'serveur',
       'julien':'libraire',
        'marie':'ingénieure'}
prenom='jacques'
profession=dic.get(prenom)#mot clé get
print(profession)
profession=dic.get(prenom,"{} n'est pas dans le registre.".format(prenom))
print(profession)

def generateur_liste(liste=[]): #liste vide à ne pas faire
    liste.extend([random.randint(1,100)for i in range(5)])
    return liste
for i in range(5):
    print(generateur_liste())
def generateur_liste(liste=None):#plutôt mettre None
    if liste is None:
        liste=[]
        liste.extend([random.randint(1,100)for i in range(5)])
    return liste
for i in range(5):
    print(generateur_liste())

#récupérer un élément inexistant d'une liste
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

#copier une liste
liste=[1,2,3,4,5]
liste_copie=liste[:]
liste_copie=liste.copy()
liste.append(5)
print(liste)
print(liste_copie)
print(id(liste))
print(id(liste_copie))

#égalité is et ==
a=5
b=5
print(a==b)
print(a is b)# de -5 à 256
a=-5000
b=-5000
print(a==b)
print(a is b)

import os
print(os.__file__)
print(__file__)
dossier_courant=os.path.dirname(__file__)
print(dossier_courant)

#join

tags=['vacances','italie','juillet',None]
nom_fichier='_'.join(filter(None,tags))#filtrer sans None
print(nom_fichier)
nom_fichier='_'.join([i for i in tags if i])
print(nom_fichier)

#chainer les comparateurs

nombre=25
if 20 <nombre< 30:
    print("le nombre est compris entre 20 et 30")

#for else

invites=['julien','marie','pierre','pascal']
for invite in invites:
    if invite =='pascal':
        print('pascal a deja été invité !')
        break #on peut rajouter break
else:
    print("pascal n'a pas été invité:(")

#enlever d'une liste
prenom='pierre'
nom='dupont'
id='1259845'
liste=[id,nom,prenom]
nomcomplet=''.join(liste)
print(nomcomplet)
prenom='pierre'
nom='dupont'
id=None
liste=filter(None, [id,nom,prenom]) #filter
liste=(e for e in (id,nom,prenom) if e)
nomcomplet=''.join(liste)

#defaultdict et OrderDict
from collections import defaultdict
mot='anticonstitutionnellement'
d={}
for lettre in mot:
    if not d.get(lettre):
        d[lettre]=1 #initialisation
    else:
        d[lettre] +=1
print(d.items())
mot='anticonstitutionnellement'
d={}
d = defaultdict(dict)
for lettre in mot:
    d[lettre]=1
print(d.items())

#utilisation de format

text='{1}{0}'.format('pierre','dupont')
print(text)
text='{:10}{}'.format('debut','fin')
print(text)
text='{:>10}{}'.format('debut','fin')
print(text)
text='{:=>10}{:=<10}'.format('debut','fin')
print(text)
text='{:+^25}'.format('debut','fin')
print(text)
text='{:.3}'.format(2.5486)
print(text)
class mavoiture(object):
    def __init__(self):
        self.couleur='rouge'
        self.marque='mercedes'
text="j'ai une {o.marque}de couleur {o.couleur}".format(o=mavoiture())
print(text)

rangées=[1,2,3,4,5,9,8,4,8]
print(*rangées,sep='-')
print('-'.join(str(r) for r in rangées))

#aplatir une liste
liste_1=[[1,2,3],[4,5,6],[7,8,9]]
ma_listeaplatie=sum(liste_1,[])
print(ma_listeaplatie)
malisteaplatiesansdouble=sorted(set(ma_listeaplatie))
print(malisteaplatiesansdouble)

#inverser les valeurs et les clés d'un dictionnaire
from pprint import pprint
LONG_NAMES={'ann_scn':'animation scene',
            'ann_pub':'animation publish',
            'sim_scn':'simulation scene'}
pprint(zip(LONG_NAMES.values(),LONG_NAMES.keys()))
SHORT_NAMES=dict(zip(LONG_NAMES.values(),LONG_NAMES.keys()))
print(SHORT_NAMES)
print(LONG_NAMES.get('ann_scn'))
