from turtle import *
import time

#position 0 de la fenetre en -340,285

def rectangle(x,y,longeur,hauteur):
    up()
    goto((-340+x),(285+y))
    #goto(x,y)
    down()
    for i in range(0,2):
        forward(longeur)
        right(90)
        forward(hauteur)
        right(90)
    up()

"""
#draw a recange
speed(11)

#construction du petis carres
cote=10

for i in range(0,65):
    for j in range(0,56):
        rectangle(i*cote,j*(-cote),cote,cote)
        if 20 < j < 25 :
            speed(1)
        else:
            speed(11)
time.sleep(5)
"""
speed(11)
for i in range(560):
    rectangle(i,-i,560-2*i,560-2*i)
time.sleep(5)