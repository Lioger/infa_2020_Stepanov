from graph import *

def krug(color, x,y, r):
    '''Draws apple at hedgehog's back
        x,y - coords circle's centre point
        r - radius of circle
        color - color of brush'''
    penColor(118,110,109)
    brushColor(color)
    circle(x,y,r)

def ovals(color, x1,y1, x2,y2):
    '''Рисует части тела и грибы (овалы)
        x1,y1, x2,y2 - coods of topleft point and of rightbottom
        color - color of brush'''
    penColor(137,134,134)
    brushColor(color)
    oval(x1,y1, x2,y2)
    
def niddles(x1,y1, x2,y2, x3,y3):
    '''Draws hedgehog's niddles
        x1,y1,x2,y2,x3,y3 - coords of triangle'''
    penColor('black')
    brushColor(40,30,30)
    polygon([(x1,y1),(x2,y2),(x3,y3),(x1,y1)])

def tree(x1,y1, x2,y2):
    '''Draws trees
        x1,y1,x2,y2 - topleft point of rectangle and rightbottom point'''
    brushColor(213,172,0)
    penColor(117,129,109)
    rectangle(x1,y1,x2,y2)

def hedgehog(x1,y1, x2):
    '''Used in function hedgehog_draw, there are made all computations
        x1,y1,x2,y2 - coords of topleft point of oval and rightbottom point'''
    y2 = y1 + ((x2-x1)*0.4)
    width=x2-x1
    height=y2-y1
    ovals((70,52,52), x1-width*0.1,y1+height*0.5, x1+width*0.1,y1+height*0.7)
    ovals((70,52,52), x2-width*0.08,y1+height*0.6, x2+width*0.04,y1+height*0.85)
    ovals((70,52,52), x1,y1, x2,y2)
    ovals((70,52,52), x2-width*0.16,y1+height*0.15, x2+width*0.16,y1+height*0.65)
    krug('black', x2,y2-height*0.63, height*0.07)
    krug('black', x2+width*0.07,y2-height*0.73, height*0.07)
    krug('black', x2+width*0.155,y2-height*0.61, height*0.04)
    ovals((70,52,52), x1,y2-height*0.3, x1+width*0.18,y2-height*0.05)
    ovals((70,52,52), x2-width*0.21,y2-height*0.2, x2-width*0.05,y2+height*0.05)

    '''Coords for niddles' triangles'''
    m=0.2 #width coefficient for steps
    n=3 #cycle
    x_1=x1+width*m
    y_1=y1+height*0.85
    
    for i in range(6):
        krug('red', x1+width*0.75,y1-height*0.2, height*0.35)
        ovals((201,114,52), x1+width*0.05,y1-height*0.4, x1+width*0.30,y1+height*0.25)
        ovals((201,114,52), x1+width*0.1,y1-height*0.45, x1+width*0.35,y1+height*0.2)
        mushroom(x1+width*0.25,y1-height, x1+width*0.7)
        for k in range(n):
            niddles(x_1+width*0.05,y_1, x_1+width*0.03,y_1-height, x_1+width*0.1,y_1)
            niddles(x_1+width*0.1,y_1+height*0.1, x_1-width*0.025,y_1-height*0.9, x_1+width*0.045,y_1-height*0.1)           
            niddles(x_1+width*0.05,y_1, x_1-width*0.25,y_1-height*0.8, x_1+width*0.075,y_1-height*0.15)
            niddles(x_1+width*0.05,y_1, x_1+width*0.15,y_1-height*0.9, x_1+width*0.1,y_1+height*0.1)
            x_1+=width*0.075

        m-=0.05
        n+=2
        x_1=x1+width*m
        y_1-=height*0.1
        
    
def mushroom(x1,y1, x2):
    '''Draws mushrooms'''
    y2=y1+0.3 *(x2-x1)
    width=x2-x1
    height=y2-y1
    ovals('white', x1+width*0.33,y1+height*0.5, x2-width*0.33, y1+width)
    ovals('red', x1,y1, x2,y2)    
    ovals('white', x1+width*0.15,y1+height*0.3, x1+width*0.25,y1+height*0.49)
    ovals('white', x1+width*0.39,y1+height*0.35, x1+width*0.49,y1+height*0.46)
    ovals('white', x1+width*0.62,y1+height*0.29, x1+width*0.72,y1+height*0.43)
    ovals('white', x1+width*0.80,y1+height*0.25, x1+width*0.94,y1+height*0.48)
    ovals('white', x1+width*0.28,y1+height*0.7, x1+width*0.4,y1+height*0.88)
    ovals('white', x1+width*0.58,y1+height*0.55, x1+width*0.68,y1+height*0.75)

def update():
    moveObjectBy(obj_1,5,0)
    moveObjectBy(obj_2,5,0)
    moveObjectBy(obj_3,5,0)
    moveObjectBy(obj_4,5,0)
    if xCoord(obj_3)>=500:
        close()
    
'''Drawing of background'''        
brushColor(40,161,90)
rectangle(0,0, 500,600)
penColor(118,110,109)
brushColor(108,93,82)
rectangle(0,350, 500,600)

'''Drawing of hedgehogs and trees''' 

hedgehog(-50,540, 50)
hedgehog(130,370, 230)
hedgehog(280,490, 420)
brushColor(213,172,0)
penColor(117,129,109)
obj_1=rectangle(75,0, 190,590)
obj_2=rectangle(350,0, 400,380)
obj_3=rectangle(0,0, 40,390)
obj_4=rectangle(450,0, 490,440)
hedgehog(420,330, 520)

mushroom(190,550, 260)
mushroom(245,575, 290)
mushroom(275,555, 325)
mushroom(320,580, 365)
mushroom(350,555, 420)
mushroom(410,570, 455)
mushroom(455,545, 525)


onTimer(update,50)
run()


