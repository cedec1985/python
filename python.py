import time
from typing import List

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




