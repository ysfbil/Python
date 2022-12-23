from turtle import Turtle, Screen
import os

screen = Screen()
screen.screensize(800, 800)
screen.title("Ayrı klasörden resim")
screen.bgcolor("lightgreen")

os.chdir("C:\\temp")
screen.register_shape("kurt.gif")

turtle = Turtle("kurt.gif")
turtle.penup()  
turtle.goto(-280, -280)
turtle.pencolor("purple")
turtle.pensize(3)
#turtle.shape("circle") #bunu açarsak kurt resmi gidiyor
turtle.pendown()

def h1(x,y):
    turtle.goto(x,y)
    turtle.write("Nerede bu koyun!!?",font=('Arial',12,'normal'),move=True)
    
def h2(x,y):
    turtle.reset()
def h3(x,y):
    turtle.write("tuşu bıraktın:)",font=('Arial',14,'bold'))
def h4(x,y):
    turtle.ondrag(None)
    #turtle.setheading(turtle.towards(x, y)) #resim dosyasında bu yönelme çalışmıyor
    turtle.goto(x, y)
    turtle.ondrag(h4)
    
screen.onclick(h1)
screen.onclick(h2,3) #3 sağ tuş, 2 orta tuş 1 varsayılan sol tuş
turtle.onrelease(h3)
turtle.ondrag(h4)

screen.mainloop()
