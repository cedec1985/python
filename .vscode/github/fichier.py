from math import *
from random import *
from builtins import int
from decorator import *
from itertools import permutations,count,takewhile,accumulate,product
from re import *  
ages={"dave":24,"Mary":42,"john":58} #dictionaries
print(ages["dave"])
primary={"red":[255,0,0],"blue":[0,255,0],"green":[0,0,255]}
print(primary["red"])
nums={1:"one",2:"two",3:"three"}
print(1 in nums,"three"in nums, 4 not in nums)
pairs={1:"apple","orange":[2,3,4],True:False,None:"true",} #method get
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, 'not in dictionary'))


for i in count(5): #itertools
    print(i)
    if i >=10:
        break

nums=list(accumulate(range(10)))
print(nums)
print(list(takewhile(lambda x:x<=6,nums)))

letters="a","b"
print(list(product(letters,range(3))))
print(list(permutations(letters)))

birth = [1981,1949,1955,1971,1975,2004] #functions list
def birth_year():
    return 2050 -len['']
for int in birth:
    result=list(map(lambda x: 2050-x,birth))
print(result)


lsit={"pierre":40,"alfred":21,"thierry":61,"laurent":38}
if "alfred" in lsit:
    print ("alfred found")
while len(lsit)>=4 or lsit%2==0:
    lsit_n=(40,21,61,38)
    if  str not in lsit_n :
        print("les noms sont",lsit)
        break
    else:
        print("impossible d'énumérer")
        
def decor (func): #decorators
    def wrap():
        print('************')
        func()
        print('************')
    return wrap

def print_text():
    print('hello')
decorated=decor(print_text)
decorated()

cruise={'ferry','paquebot','ocean','sea','oasis of the seas'.upper()} #sets
cruise.add('jet-ski')
holiday={'beach','sand','sunset','cocktail','pool'.upper(),'sea'}
holiday.add('sleep')
print(cruise | holiday,cruise-holiday)

def countdown(): #generators
    i=5
    while i>0:
        yield i
        i -=1
for i in countdown():
    print(i)


def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i
print(list(numbers(11)))
def apply_twice (func,arg):#functional programming
    return func(func(arg))
def add_five(x):       
    return x+5
print(apply_twice(add_five,2))
try:   #exceptions
    print(8)
    assert (8/0)
except ZeroDivisionError:
    print("division par 0")
finally:
    print('code will run no matter what')

class student:  #POO #methods
    def __init__(self,name,level):
        self.name=name
        self.level=level
    def biology(self):
        self
        print(self.name)
obj=student('john says hi',3)
print(obj.name)

class baby:  #inheritance
    def bark(self):
        print('helllloooo')
class school(baby):
    def park(self):
        print('areeeeuuh')
class teen(baby):
    def accent(self):
        print('ooooooohey')
c=teen()
c.accent()
c=school()
c.park()
c=baby()
c.bark()
  #re
ph="la mer a une température idéale"
pattern=r"mer"
if re.match(pattern,"mer"):
    print('Match') 
else:('No match')








