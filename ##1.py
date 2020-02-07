from graph import *

def krug(zalivka,x,y,rad):
    penColor('black')
    brushColor(zalivka)
    circle(x,y, rad)
def brov(x1,y1,x2,y2,x3,y3,x4,y4):
    brushColor('black')
    polygon([(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x1,y1)])
def vesn(a,b,radius):
    brushColor('orange')
    penColor('orange')
    circle(a,b,radius)

krug('yellow',250,250,200)
krug('red',150,200,40)
krug('black',150,200,15)
krug('red',350,200,30)
krug('black',350,200,15)
brov(50,80,60,65,220,180,210,195)
brov(450,120,440,105,280,180,290,195)
brushColor('black')
rectangle(150,350,350,380)
m=70
n=270
for p in range(2):
    for y in range(3):
        for i in range(5):
            vesn(m,n,5)
            m+=25
        n+=25
        m-=100
    m=270
    n=270
run()
