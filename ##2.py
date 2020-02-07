from graph import *

''' def oval(x,y, shirina,vysota):
    step=list()
    for i in range(50):
        koord=(x+shirina,y+vysota)
        step.append(koord)
        shirina+=0.15
        vysota-=0.15
    for q in range(50):
        koord=(x+shirina,y+vysota)
        step.append(koord)
        shirina+=0.15
        vysota+=0.15
    for w in range(50):
        koord=(x+shirina,y+vysota)
        step.append(koord)
        shirina-=0.15
        vysota+=0.15
    for e in range(50):
        koord=(x+shirina,y+vysota)
        step.append(koord)
        shirina-=0.15
        vysota+=0.15
    polygon(step) '''

def krug(color,x,y,r):
    penColor(150,150,170)
    brushColor(color)
    circle(x,y,r)
    
def triangle(x1,y1,x2,y2,x3,y3):
    penColor('black')
    brushColor(40,30,30)
    polygon([(x1,y1),(x2,y2),(x3,y3),(x1,y1)])
    
brushColor(0,175,100)
rectangle(0,0,500,600)
penColor(150,150,150)
brushColor(110,90,90)
rectangle(0,350,500,600)
brushColor(230,200,0)
penColor(180,160,0)
rectangle(0,0,40,390)
rectangle(75,0,190,590)
rectangle(350,0,400,380)
rectangle(450,0,490,440)
krug((90,70,70),295,515,12)
krug((90,70,70),405,515,12)
krug((90,70,70),350,500,50)
krug((90,70,70),400,500,30)
krug('black',405,495,5)
krug('black',420,485,5)
krug('black',430,500,3)
krug((90,70,70),310,540,12)
krug((90,70,70),390,540,12)
k=0
i=0
x=300
y=530
z=9
while k in range(6):
    while i in range(z):
        triangle(x,y,x+8,y,x+4,y-60)
        x+=8
        i+=1
    y-=10
    i=0
    x=300
    k+=1
    z+=1
krug('red',380,470,15)
krug((200,120,50),320,470,15)
krug((200,120,50),330,470,15)
krug('white',350,450,13)
krug('red',360,430,20)

k=0
i=0
x=350
y=435
while k in range(2):
    while i in range(4):
        krug('white',x,y,3)
        x+=8
        i+=1
    y-=8
    i=0
    x=345
    k+=1

run()

