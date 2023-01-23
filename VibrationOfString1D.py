#Author Kamalakannan V
#created on 23-01-2023
import matplotlib.pyplot as plt
import numpy as np

#def plot(x, timeStep, YMaxDis):
x= 10
YMaxDis=1

curveX=[]
currentY=[]
PreviousY=[]
nextY=[]
for j in np.arange(0,x,.1):
    curveX.append(j)
    currentY.append((YMaxDis/x)*j)
    PreviousY.append((YMaxDis/x)*j)
for k in np.arange(x,100,.1):        
    curveX.append(k)
    currentY.append((YMaxDis/(x-100))*k+((100*YMaxDis)/(100-x)))
    PreviousY.append((YMaxDis/(x-100))*k+((100*YMaxDis)/(100-x)))
nextY= currentY[:]
for i in range(100000):
    nextY=currentY[:]
    for l in range(1, len(curveX)-1): 
        nextY[l]=((.02*0.02)/(0.1*0.1))*(currentY[l+1]-2*currentY[l]+currentY[l-1])+2*currentY[l]-PreviousY[l]
    if((i%50)==0):
        plt.clf()
        plt.plot(curveX, nextY)
        plt.ylim(-1,1)
        plt.pause(.001)
    PreviousY=currentY[:]
    currentY=nextY[:]
    nextY=[]               

plt.show() 
  

  


