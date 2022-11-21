# pip install pgzero
import pgzrun
from random import randint

elma=Actor("apple")

def draw():
    screen.clear()
    elma.draw()

def elma_konumu():
    elma.x=randint(10,800)
    elma.y=randint(10,600)

def on_mouse_down(pos):
    if elma.collidepoint(pos):
        print("Tebrikler")
        elma_konumu()
    else:
        print("kaçırdın!")
        quit()
    

elma_konumu()
pgzrun.go()
