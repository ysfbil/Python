from turtle import *
import time

#silinebilir yazı
def yaz(tortoise, name, font=("Arial", 20, "normal"), align="center",t=5, reuse=None):
    eraser = Turtle() if reuse is None else reuse
    eraser.hideturtle()
    eraser.up()
    eraser.setposition(tortoise.position())
    eraser.write(name, font=font, align=align)
    time.sleep(t)
    eraser.clear()

def kontrol():
  global sol1,sol2,sol3,sol4,txt,kilit
  #yaz(txt,"sol1="+str(sol1)+" sol2="+str(sol2)+" sol3="+str(sol3)+" sol4="+str(sol4),t=3)
  if (sol1==sol3 and (sol1!=sol4) ):
    yaz(txt,"KOYUN OTU YEDİ - KAYBETTİN :(")
    kilit=True
    baslangic()
  elif (sol1==sol2 and (sol1!=sol4)):
    yaz(txt,"KURT KOYUNU YEDİ - KAYBETTİN :(")
    kilit=True
    baslangic()
  elif (not sol1 and not sol2 and not sol3 and not sol4):
    yaz(txt,"TEBRIKLER KAZANDIN :)")
    kilit=True
    baslangic()
  ksol4=sol4

def karsiyaGecipAl(sol):
  global Solkiyi,sol4,t4x,t4y,ksol4
  if sol4!=sol:
    if sol:
      t4.goto(t4x,t4y) #karşıya gidip soldan al
      sol4=True
      kontrol()
    else:
      t4.goto(Solkiyi,t4y) #karşıya gidip sağdan al
      sol4=False
      kontrol()

#koyunun geçiş fonksiyonu
def gec1(x,y):
  kontrol()
  global Solkiyi,sol1,sol4,t1x,t1y,t4x,t4y,kilit
  karsiyaGecipAl(sol1)    
      
  if kilit:
    kilit=False
    return
  
  if (sol1):
    t1.goto(t4x,t4y)   
    while (t1.xcor()<Solkiyi):    
      t1.forward(4)         
      t4.forward(4)    
    sol1=False
    sol4=False
    t1.goto(Solkiyi+100,t1y)
    koyunDrm=1
  else:
    t1.goto(Solkiyi,t4y)
    while (t1.xcor()>t4x):    
      t1.backward(4)         
      t4.backward(4)    
    sol1=True
    sol4=True
    t1.goto(t1x,t1y)
    koyunDrm=0
  kontrol()


   

#kurdun geçiş fonksiyonu  
def gec2(x,y):
  kontrol()
  global Solkiyi,sol2,sol4,t2x,t2y,t4x,t4y,kurtDrm,kilit
  karsiyaGecipAl(sol2)

  if kilit:
    kilit=False
    return      
    
  if (sol2):
    t2.goto(t4x,t4y)   
    while (t2.xcor()<Solkiyi):    
      t2.forward(4)         
      t4.forward(4)    
    sol2=False
    sol4=False
    t2.goto(Solkiyi+100,t2y) #kurt sağ kıyıya geçti
    kurtDrm=1
  else:
    t2.goto(Solkiyi,t4y)
    while (t2.xcor()>t4x):    
      t2.backward(4)         
      t4.backward(4)    
    sol2=True
    sol4=True
    t2.goto(t2x,t2y) #kurt sola geçti
    kurtDrm=0
  kontrol()


#otun geçiş fonksiyonu

def gec3(x,y):
  kontrol()
  global Solkiyi,sol3,sol4,t3x,t3y,t4x,t4y,kilit
  karsiyaGecipAl(sol3)

  if kilit:
    kilit=False
    return    
    
  if (sol3):
    t3.goto(t4x,t4y)   
    while (t3.xcor()<Solkiyi):    
      t3.forward(4)         
      t4.forward(4)    
    sol3=False
    sol4=False
    t3.goto(Solkiyi+100,t3y) #ot sağa geçti
    otDrm=1
  else:
    t3.goto(Solkiyi,t4y)
    while (t3.xcor()>t4x):    
      t3.backward(4)         
      t4.backward(4)    
    sol3=True
    sol4=True
    t3.goto(t3x,t3y) #ot sola geçti
    otDrm=0
  kontrol()

def baslangic():
  global sol1,sol2,sol3,sol4,t1,t2,t3,t4,t1x,t1y,t2x,t2y,t3x,t3y,t4x,t4y,kilit
  
  t1.goto(t1x,t1y)
  t2.goto(t2x,t2y)
  t3.goto(t3x,t3y)
  t4.goto(t4x,t4y)

  t1.showturtle()
  t2.showturtle()
  t3.showturtle()
  t4.showturtle()

  t1.speed(2)
  t2.speed(2)
  t3.speed(2)
  t4.speed(2)

  sol1,sol2,sol3,sol4=True,True,True,True


#ekran arkaplanını ayarlıyoruz.
scr = Screen()
scr.setup(800, 614)

kilit=False

t1=Turtle()
t2=Turtle()
t3=Turtle()
t4=Turtle()
txt=Turtle()

# resimler gif olmalı
kurt = "kurt.gif"
koyun="koyun.gif"
ot="ot.gif"
kayik="kayik.gif"

scr.addshape(kurt)
scr.addshape(koyun)
scr.addshape(ot)
scr.addshape(kayik)

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()
t4.hideturtle()
txt.hideturtle()

yaz(txt,"Kurt, koyun ve otu zarar görmeden karşıya geçiriniz")
yaz(txt,"Unutmayın! Kayıkçı varken kimse kimseyi yiyemiyor.")
yaz(txt,"BAŞARILAR :)",t=3)

scr.bgpic("nehir.gif")

t1.shape(koyun)
t2.shape(kurt)
t3.shape(ot)
t4.shape(kayik)


t1.penup()
t2.penup()
t3.penup()
t4.penup()

t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)

t1x,t1y=-250,60
t2x,t2y=-230,-100
t3x,t3y=-250,150
t4x,t4y=-100,0
Solkiyi=200

baslangic()

t1.onclick(gec1)
t2.onclick(gec2)
t3.onclick(gec3)

scr.mainloop()

#t1.setx(100)
#t1.setx(100)




