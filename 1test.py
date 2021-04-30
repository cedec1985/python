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
        destf=mult+result+solution
        return mult,result,solution
print(count_char(x))
print(len(count_char(x)))
# add an item to a list or substract from a list
x_1=6
def eo (x_1):
    if x_1 <7:
        x_1=list_2.append((x_1)*2)
        return list_2
    elif x_1==6:
        x_1=list_2.pop(1)
        return list_2
    else:
        print("rien à ajouter à cette liste",list_2)
print(eo(x_1))
i="python"

        