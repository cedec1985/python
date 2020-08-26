
from math import *
from random import *
items=["a","b","c","d","e"]
n=len(items)                                #len=énumération dans cet ordre = e1
for i in range(n):  
    print(str(i+1)+"."+items[i])
for i in range(10):                                     # e2 for
    for a in range(10):
        if a <=i:
            print("*", end='')                           #pas de retour à la ligne avec end
        else:
            print('', end='')
    print()
num=input("enter symbol or num")                           #e3
for a in range (1,7):
    print(a*num)
numbers= list (range(10))                                #e4
print(numbers)
list=[1,1,2,3,5,8,13]
print(list[list[4]])                    # le quatrième élément de la liste qui ne se répète pas =e5
for i in range(10):
    if not i%2 ==0: 
        print(i+1)

list=[1,2,3,4]                                          #e6
if len(list)%2 ==0:
    print (list[0])

print(27**1/3)
print(27**(1/3))
print(7//2)
print(4%2)                                          #renvoie le reste de la division
print(-14//-2)
print(5**0+7)
print(13%3)
n=5
print(type(n))                              #renvoie le type ou la classe (booléen, float ou int)
n=1/2
print(type(1/2))
n<1
print(type(n<1))
a=4
print(str(1+2+3*a))
print("bon"+"jour")                              #concaténation
print(str("bon"+"jou"))
x=2
print(eval("x**8"))                             #renvoie un nombre
print(str(1+2+3+4))                        #renvoie une chaine de caractères
a=45>50
print(a)
cote=10
aire=cote*cote
print("la surface dont le cote vaut",cote,"est égal à",aire)
a=3
print(a**3,a*2,a-1,sep="/")                                                       #sep précise le type de séparateur
n=input("entrez votre nom")
print ("bonjour",n)
x=eval(input("entrez un nombre"))
print("le double de",x,"est",2*x)
n1=eval(input("note 1:"))                                   #eval peut transformer une chaine de caractères en un nombre
n2=eval(input("note 2:"))
n3=eval(input("note 3:"))
m=(n1+n2+n3)/3
print ("la moyenne est de :",m)
n=eval(input("nombre d'entrées :"))
p1=3*n
p2=2*n+5
if p1<p2:
    print("le tarif 1 est plus avantageux")
else:
    print("le tarif 2 est plus avantageux")
n=eval(input("entrez le nombre de kilomètres parcourus"))
p=46
if n>200:
    p=p+(n-200)*0.14
print("le prix à payer est de :",p,"euros")
p=p*1.2
print("le prix à payer T.T.C est de :",p,"euros")
# calculs mathématiques

x=eval(input("entrez un nombre"))
if x**2-5*x==0:                         #solution d'une équation
   print(x,"est solution de l'équation")
else:
   print(x,"n'est pas solution de l'équation")
x=eval(input("de quel nombre souhaitez-vous l'image"))#image d'une fonction
if x==2:                                    
   print(x,"n'est pas dans l'ensemble de définition de f.")
else:
   f=(2*x+1)/(x-2)
   print("l'image de",x,"est",f)
a,b,c,d=eval(input("entrez quatre nombres"))
if c!=0:                                                     #fonction mathématique
    if a*d-b*c==0:
        print("la fonction f est une fonction constante")
    else:
        print ("la fonction f est une fonction homographique")
else:
    if d==0:
        print("impossible de définir la fonction")
    else:
        print("la fonction est une fonction affine")
a,b=75,45                                                        #le PGCD avec while cond.
print("le pgcd de",a,"et",b,"vaut",end="")
while a!=b:
    if a>b:
        a,b=b,a-b
    else:
        a,b=a,b-a
print(a)
                                                        # for var in range (début,fin,pas) incond.
for lettre in "python":
    print(lettre)
for i in(1,4,5,6,7,9):
    print(i)
for i in range(0,10,1):
    print(i)
                                                        #exemple de while incond.
s=eval(input("somme à épargner par mois"))
prix=13900
épargne=2000
mois=0
while épargne<prix:
    mois=mois+1
    épargne=épargne+s
    prix=prix*0.98
    print("à la fin du mois",mois,"il a",épargne,"et la voiture coute",prix)
    print("il peut acheter sa voiture à la fin du mois",mois,"ième mois")
                                                        
ISBN=eval(input("entrez un code isbn"))                         #code ISBN
chiffres=ISBN//10
cle1=ISBN%10
cle2=0
for rang in range(12,0,-1):                     #-1 =  1 pas inverse 
    if rang%2==0:                               # rang pair
        cle2=cle2+3*(chiffres%10)
    else:
        cle2=cle2+chiffres%10                   #rang impair
    chiffres=chiffres//10
cle2=(10-(cle2%10)%10)
if cle1==cle2:
    print("code correct")
else:
    print("code incorrect")
for u in range (1,10):                       #palindrome de nombres
    for d in range(10):
        for c in range(10):
            n=u*10000+d*1000+c*100+d*10+u
            r=round(sqrt(n))
            if r**2==n and r//100 ==r%10:
                print(r, "²=",n)
for a in range(1,8364):                 #les diviseurs d'un nombre
    if 8364%a==0:
        b=8633//a
        print("8633=",a,"x",b)
for a in range (1,10):
    for b in range(1,10):
        for c in range(1,10):
            if (10*a+b)*c == (10*b+c)*a and a!=b:
                print(a,b,"/",b,c,"=",a,"/",c,sep="")
for x in range(94):                             
    for y in range(94):
        if x**2+4*y**2==8633:
            print(x,",",y)
niveau=eval(input("nombre de niveaux"))#chateau de cartes
cartes=2
for e in range(1,niveau):
    cartes=cartes+3*e+2
    print("il faut",cartes,"cartes pour fabriquer",niveau,"niveaux")
cartesmax=eval(input("nombre de cartes max"))
e=0
cartes=0
while cartes<cartesmax:
    cartes=cartes+3*e+2
    e=e+1
print("on peut faire maximum",e-1,"niveaux")
N=1000
somme,sommeCarre=0,0
for i in range(N):                          #probabilité de lancers avec des dés
    de1=randint(1,6)
    de2=randint(1,6)
    diff=abs(de1-de2)
    somme=somme+diff
    sommeCarre=sommeCarre+diff**2
E=somme/N
s=sqrt(sommeCarre/N-E**2)
print("estimation de l'espérance",E)
print("estimation de l'écart type",s)
nb6,nbcas=0,0
for derouge in range(1,7):
    for debleu in range(1,7):
        for devert in range(1,7):
            if derouge+debleu+devert==6:
                nb6=nb6+1
                nbcas=nbcas+1
print("nombre de fois où l'on a eu 6",nb6)
print("nombre de cas",nbcas)

nb1,nb2,nb3,nb4,nb5,nb6=0,0,0,0,0,0
i=0
while i<10000:
    de=floor(6*random()+1)
    if de==1:
        nb1=nb1+1
    elif de==2:
        nb2=nb2+1
    elif de==3:
        nb3=nb3+1
    elif de==4:
        nb4=nb4+1
    elif de==5:
        nb5=nb5+1
    elif de==6:
        nb6=nb6+1
    else:
        print("valeur tirée",de,".impossible")
        i=20000
    i=i+1
if i<20000:
    print("fréquence des 1",round(nb1/i,2))
    print("fréquence des 2",round(nb2/i,2))
    print("fréquence des 3",round(nb3/i,2))
    print("fréquence des 4",round(nb4/i,2))
    print("fréquence des 5",round(nb5/i,2))
    print("fréquence des 6",round(nb6/i,2))
                                                        #les fonctions
def f(x):
    if x==3:
        return "X"
    else:
        return (x-1)/(x-3)
for x in range(0,6):
    print(x,f(x),sep="\t")
