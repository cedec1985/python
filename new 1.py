list_1=[1,2,3,4,5,6,7,8]
x=2
for y in list_1:
    y=len(list_1)
    dep=x*y
    for x in list_1:
        dep_1=x*y
        x+=dep
    if list_1[:]!=float:
        print(dep)
else: 
    print(len(list_1))
for i in range(1,6):
    for j in range (1,4):
        print(i+j)
#multiply each item of the list by the next one
list_2=[2,3,4,5]
x=list_2[0]
count=0
def count_char(x):
    for count in list_2:
        count+=1
        mult=x*count
        y=x+2
        result=mult*y
        z=y+1
        solution=z*result
        return mult,result,solution
print(count_char(x))
def tilt(x,y):
    x=[1,2,3]
    y=[1,2,4]
    for l in x:
        for m in y:
            if l%2==0 and m%2==0 :
                dep=l*m
                return dep
print(tilt(x,y))
class factory():
    def calc(self,y=int):
        x=("2","3","4")
        x_1=eval(x[0])
        print(x_1)
class angel(factory):
    def winds(self):
        pilz=("4","5")
        y=eval(pilz[1])
        print(y)
class human(angel):
    def legs(self):
        arc=("6","7")
        z=eval(arc[0])
        print(z)
c=factory()
c.calc()
b=angel()
b.winds()
d=human()
d.legs()
class new:
    def __init__(self,even,odd):
        self.even=even
        self.odd=odd
    def addition(self):
        return self.even+self.odd
    @classmethod 
    def add_it(cls,number):
        return cls(number,number)
a=new.add_it(5)
print(a.addition())

