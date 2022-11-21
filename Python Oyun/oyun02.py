#https://pygame-zero.readthedocs.io/en/stable/builtins.html

import pgzrun
from random import randint

WIDTH=800
HEIGHT=570
puan=0

arkaplan=Actor("surface")
arkaplan.topleft=0,0

mekik=Actor("apollolander")
mekik.pos=randint(100,600),100

beep = tone.create('A3', 0.5)

TARGET=Rect((randint(100,750),randint(380,500)),(50,50)) #x=100-700 arası, y=380, 50x50 büyüklüğünde

def draw():
    screen.clear()
    arkaplan.draw()
    mekik.draw()
    screen.draw.textbox("Aracı aya indir",(0,0,200,50),shadow=(1.0,1.0),
                        scolor="blue") #sol,üst,en,yükseklik
    screen.draw.rect(TARGET,(255,0,0))
    screen.draw.textbox("hedef",TARGET,color="blue",gcolor="green")
    screen.draw.textbox("Puan: "+str(puan),(550,0,100,50))

def update():
    if keyboard.right:
        mekik.pos=(mekik.x+5,mekik.y)
    if keyboard.left:
        mekik.pos=(mekik.x-5,mekik.y)
    if keyboard.up:
        mekik.pos=(mekik.x,mekik.y-10)

    mekik.y=mekik.y+5

    mekik_indimi()

    

def mekik_indimi():

    global puan
    global TARGET
    
    if mekik.colliderect(TARGET):
        puan +=1
        mekik.pos=randint(100,600),100
        TARGET=Rect((randint(100,750),randint(380,500)),(50,50))
        sounds.bravo.play()
        

    elif mekik.y>550:
        mekik.pos=randint(100,600),100
        puan -=1
        beep.play()
    

pgzrun.go()

