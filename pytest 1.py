x=({0,2,5,4,8,2,2,6,7,9})
print(len(list(x)))
y =({1,3,5,4,2,2,1,0})
if (y==8,bool=="true"):
    print("parfait",list(y),sep="=>")
z=({0,3,3,3,4,5,8})
print(len(set(z)))
def f(i):
    for i in range(5):
        i+=1
        return i
try:
    f(2)
except: 
    IndexError
finally:
    print("il y a une erreur dans le programme")
import re
yil={'a':"4",'b':"5",'c':"4",'d':"3",'e':"8"}
f=r'a'
sel=re.search('a',f)
print(f)
sel=re.findall("4",f)
print(f)
sel=re.match("4",f)
print(f)
xena=[4,5,4,3,8]
