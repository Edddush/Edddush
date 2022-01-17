#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 12:59:14 2018

@author: coco,Ryan,Eddy
"""
import pygame, sys
from pygame.locals import *
import pygame.locals
from pygame import key,event

pygame.init()
fpsClock = pygame.time.Clock()
SIZE = 4
BLOCKSIZE=100
MAX=SIZE*BLOCKSIZE
_GameEnd=None
_GameOver=None
windowSurfaceObj = pygame.display.set_mode((MAX,MAX+100))
pygame.display.set_caption('2048')

#color
redColor = pygame.Color(255,0,0)
greenColor = pygame.Color(0,255,0)
blueColor = pygame.Color(0,0,255)
whiteColor = pygame.Color (255,255,255)
lightblue = pygame.Color(173, 216, 230)
lightgreen = pygame.Color(132,231,142)
lighterblue = pygame.Color(235,255,255)
grey =  pygame.Color(145,141,142)
gold =  pygame.Color(255,215,0)
black=  pygame.Color(0,0,0)
granite = pygame.Color(131,126,124)
box1 =  pygame.Color(201,196,194)
color2 =(229,228,227)
color4 = pygame.Color(229,182,147)

colors = {2:(159,193,250),4:(0,176,250),8:(31,83,248),16:(130,74,255),
          32:(180,28,255),64:(255,81,119),128:(255,219,90),
          256:(229,200,70),512:(229,180,50),1024:(229,170,40),2048:(229,160,20),
          4096:(0,0,0),8192:(0,0,100),16384:(30,0,0),32768:(60,0,0)}
mousex,mousey = 0,0

fontscore = pygame.font.SysFont('verdana',40)
fontObj  = pygame.font.SysFont('verdana',32)
fontObj2  = pygame.font.SysFont('verdana',32)
fontObj16  = pygame.font.SysFont('verdana',28)
fontObj128  = pygame.font.SysFont('verdana',26,bold=True)
fontObj1024  = pygame.font.SysFont('verdana',24,bold=True)
fontObj16384  = pygame.font.SysFont('verdana',23,bold=True)
fontObjSmall  = pygame.font.SysFont('verdana',22,bold=False)
fonts =[fontObj2,fontObj16,fontObj128,fontObj1024,fontObj16384,fontObjSmall]
map1=[[0 for i in range (5)]for j in range(5)]
score=0

lineArray = []
for a in range(0,MAX,BLOCKSIZE) :
    lineArray.append( (0,a))
    lineArray.append((MAX,a))
    lineArray.append((MAX,a+BLOCKSIZE))
lineArray.append((MAX,0))
lineArray.append((0,0))
for a in range(0,MAX,BLOCKSIZE) :
    lineArray.append( (a,0))
    lineArray.append((a,MAX))
    lineArray.append((a+BLOCKSIZE,400))
print(lineArray)

def moveleft():
    global r,score,map1
    for i in range (1,5):
        for j in range (1,5):
            if map1[i][j] == 0:
                for k in range (j+1,5):
                    if map1[i][k] != 0:
                        map1[i][j] = map1[i][k]
                        map1[i][k] = 0
                        break
    for i in range (1,5):
        if map1[i][1] == map1[i][2]:
            map1[i][1] = 2*map1[i][1]
            score += map1[i][1]
            if map1[i][3]== map1[i][4]:
                map1[i][2]= 2*map1[i][3]
                score += map1[i][2]
                map1[i][3]= 0
                map1[i][4]= 0
            else:
                map1[i][2]= map1[i][3]
                map1[i][3]=map1[i][4]
                map1[i][4]=0
        else:
            if map1[i][2] == map1[i][3]:
                map1[i][2] = 2*map1[i][2]
                score += map1[i][2]
                map1[i][3] = map1[i][4]
                map1[i][4] = 0 
            else:
                if map1[i][3] == map1[i][4]:
                    map1[i][3] = 2*map1[i][3]
                    score += map1[i][3]
                    map1[i][4] = 0 

     
def moveright():
    global r,score,map1
        #move right 
    for i in range (1,5):
        for j in range (4,0,-1):
            if map1[i][j]==0:
                for k in range(j-1,0,-1):
                    if map1[i][k]!= 0:
                        map1[i][j]= map1[i][k]
                        map1[i][k]=0
                        break
        
        #add the numbers
    for i in range(1,5):
            if map1[i][4]== map1 [i][3]:
                map1[i][4]+=map1[i][3]
                score += map1[i][4]
                if map1[i][1]==map1[i][2]:
                    map1[i][3]=2*map1[i][2]
                    score += map1[i][3]
                    map1[i][1]=0
                    map1[i][2]=0
                else: 
                    map1[i][3]=map1[i][2]
                    map1[i][2]= map1[i][1]
                    map1[i][1]=0
            else:
                if map1[i][3]== map1[i][2]:
                    map1[i][3]+=map1[i][2]
                    score += map1[i][3]
                    map1[i][2]=map1[i][1]
                    map1[i][1]=0
                else:
                    if map1 [i][1]==map1[i][2]:
                        map1[i][2]+=map1[i][1]
                        score += map1[i][2]
                        map1[i][1]=0
    
def movedown():
    global r,score,map1
    for i in range (4,0,-1):
        for j in range(1,5):
            if map1[i][j]==0:
                for k in range (i-1,0,-1):
                    if map1[k][j] != 0:
                       map1[i][j]= map1[k][j]
                       map1[k][j]=0
                       break
    #Adding(In progress)

    for j in range (1,5):
            if map1[4][j]== map1 [3][j]: 
                map1[4][j]+=map1[4][j]
                score += map1[4][j]
                if map1[1][j]==map1[2][j]:
                    map1[3][j]=2*map1[2][j]
                    score += map1[3][j]
                    map1[2][j]=0
                    map1[1][j]=0
                else: 
                    map1[3][j]=map1[2][j]
                    map1[2][j]=map1[1][j]
                    map1[1][j]=0
            else:
                if map1[3][j]== map1[2][j]:
                    map1[3][j]+=map1[2][j]
                    score += map1[3][j]
                    map1[2][j]=map1[1][j]
                    map1[1][j]=0
                
                else:
                    if map1 [1][j]==map1[2][j]:
                        map1[2][j]+=map1[1][j]
                        score += map1[2][j]
                        map1[1][j]=0
    
def moveup():
    global score,map1
    for i in range (1,5):
        for j in range(1,5):
            if map1[i][j] ==0:
                for k in range (i+1,5):
                    if map1[k][j]!=0:
                        map1[i][j]=map1[k][j]
                        map1[k][j]=0
                        break
    # adding (In progress)
    for j in range (1,5):
            if map1[1][j]== map1 [2][j]:
                map1[1][j]+=map1[2][j]
                score += map1[1][j]
                if map1[3][j]==map1[4][j]:
                    map1[2][j]=2*map1[3][j]
                    score += map1[2][j]
                    map1[3][j]=0
                    map1[4][j]=0
                else: 
                    map1[2][j]=map1[3][j]
                    map1[3][j]=map1[4][j]
                    map1[4][j]=0
            else:
                if map1[3][j]== map1[2][j]:
                    map1[2][j]+=map1[3][j]
                    score += map1[2][j]
                    map1[3][j]=map1[4][j]
                    map1[4][j]=0
                
                else:
                    if map1 [3][j]==map1[4][j]:
                        map1[3][j]+=map1[4][j]
                        score += map1[3][j]
                        map1[4][j]=0

def processMovement(myList:list,directive:int):
    global map1
    print(myList)
    newList=[]
    for i in range (1,5):
        for j in range(1,5):
            map1[i][j]=0
    for (x,y,z) in myList:
        map1[(y//BLOCKSIZE)+1][(x//BLOCKSIZE)+1]=z

    if directive == pygame.K_DOWN:  
        movedown()
    if directive == pygame.K_UP:
        moveup()

    elif directive == pygame.K_LEFT:  
        moveleft()
    elif directive == pygame.K_RIGHT:  
        moveright()

    for i in range (1,5):
        for j in range(1,5):
            if map1[i][j]!=0:
                newList.append([(j-1)*BLOCKSIZE,(i-1)*BLOCKSIZE,map1[i][j]])

    standStill = True if sorted(myList)==sorted(newList) else False
    return newList,standStill

def getRandBox(myList):
    simpleLock=[]
    simpleEmpty=[]
    for [x,y,z] in myList:
        simpleLock.append((y//100)*4+x//100)
    #simpleEmpty=[x for x in range(0,16) if x not in simpleLock]
    for x in range(0,16):
        if(x not in simpleLock):
            simpleEmpty.append(x)
    import random
    x=random.choice(simpleEmpty)
    z = random.randint(0,10)
    #z = 2 if z <= 9 else 4
    if z<=9:
        z=2
    else:
        z=4
    return  [(x%4)*100,(x//4)*100,z]

def drawBox(box,border=None):
    x,y,z=box

    if(border==None):
        border= color2
    fillColor=colors[z]

    myRect=pygame.draw.rect(windowSurfaceObj,border,(x+2,y+2,98,98),0)
    windowSurfaceObj.fill(border,myRect)
    windowSurfaceObj.fill(fillColor, myRect.inflate(-5, -5))
    msg=str(z)

    #msgSurfaceObj = fontObj.render(msg,True,granite if z<16 else whiteColor)
    msgSurfaceObj = fontObj.render(msg,True,whiteColor)
    msgRectobj = msgSurfaceObj.get_rect()

    msgRectobj.center = (x+50,y+52)
    windowSurfaceObj.blit(msgSurfaceObj,msgRectobj)
    
def drawscore():
    msg="score: "+str(score)
    msgSurfaceObj = fontscore.render(msg,True,whiteColor)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.center = (200,450)
    windowSurfaceObj.blit(msgSurfaceObj,msgRectobj)
    msgquit="Quit: Esc"
    msgSurfaceObj = fontObjSmall.render(msgquit,True,redColor)
    msgRectobj = msgSurfaceObj.get_rect()
    msgRectobj.center = (350,480)
    windowSurfaceObj.blit(msgSurfaceObj,msgRectobj)
    
def dead(myList:list):
    map2=[[0 for i in range (5)] for j in range(5)]
    for i in range (1,5):
        for j in range(1,5):
            map2[i][j]=0
    for (x,y,z) in myList:
        map2[(y//BLOCKSIZE)+1][(x//BLOCKSIZE)+1]=z
    flag=0
    for i in range(1,5):
        for j in range(1,4):
            if(map2[i][j]==map2[i][j+1]):
                flag=1
    for j in range(1,5):
        for i in range(1,4):
            if(map2[i][j]==map2[i+1][j]):
                flag=1
    
    for i in range(1,5):
        for j in range(1,5):
            print(map2[i][j],end=" ")
        print(" ")
    print(flag)
    
    if flag==0:
        pygame.display.update()
        return True
    return False
    
'''
file = open("testfile.txt", "r")
scores1 =[]

for j in range(0,10):
    pp=int(file.readline())
    scores1.append(pp)


file.close()

print(scores1)
    
print("The highest score:",scores1[0])
'''


locked=[]
new  = (getRandBox(locked))
print("first pick:",new)
locked.append(new)
action = None
flag = 0

while True:
    
    windowSurfaceObj.fill(lightgreen)
    pygame.draw.lines(windowSurfaceObj,lighterblue,False,lineArray,2)
    
    if len(locked)==1:
        drawBox(locked[-1],gold)
    
    drawscore()

    for event in pygame.event.get():
        if flag == 2:
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
                elif event.key in (pygame.K_LEFT,pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) :
                    print(" game is over. esc")

        if flag == 1:
            print(" game is over. esc")
            flag = 2
        if flag == 0:
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_LEFT,pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN) :
                    standStill=False
    
                    print( "Arrow Key pressed.",event.key)
                    action = event.key
                    locked,standStill=processMovement(locked,event.key)
                    print("\n\n",score,"\n\n")
                    
                    try:
                        pygame.display.update()
                        fpsClock.tick(30)
                    except:
                        flag+=0
                    
                    if not standStill:
                        #Total = Total + score
                        new =getRandBox(locked)   #get random box
                        locked.append(new)       #append to locked
                        #print("random picK:",new)
                        if(len(locked)==16):
                            print(dead(locked))
                            pygame.display.update()
                            if(dead(locked)==True):
                                pygame.display.update()
                                #drawBox(locked[-1],gold)
                                #pygame.display.update()
                                '''
                                scores1[9]=score
                                #print(scores1)
                                scores1.sort()
                                scores1.reverse()
                                #print(scores1)
                                open_file=open("testfile.txt","w")
                                for j in range(0,10):
                                    open_file.write(str(scores1[j]))
                                    open_file.write("\n")
                            
                                open_file.close()
                                '''
                                print("Gameover")
                                flag=1
    
    
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(pygame.QUIT))
    if action:
        for i in locked[:-1]:
            drawBox(i,grey)

        drawBox(locked[-1],gold)
    try:
        pygame.display.update()
        fpsClock.tick(30)
    except:
        print()
