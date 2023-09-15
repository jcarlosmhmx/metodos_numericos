#!/usr/bin/env python
#----------------------Funciones------------------------
def f(y):
    
    #valor = 1-(g**2)*(b)/(g*(3*y+(y**2/2)**3))
    return  1-((g**2)/(g*((Ac(y))**3))*b) 
    

def Ac(y):
    return 3*y+((y**2)/2)
#----------------------Variables------------------------
q = 20.00
g = 9.81

#Ac = 3*y+((y**2)/2)

y=2
b = 3 + y


print(b," ",y," ",Ac(y)," ",f(y))