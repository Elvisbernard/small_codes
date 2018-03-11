# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 15:24:37 2018

@author: Elvis
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


''' here are the three different functions I have used to calculate the distance'''

def manhattan():
    df['distance_a']=abs(df.x-center_A[-1][0])+abs(df.y-center_A[-1][1])
    df['distance_b']=abs(df.x-center_B[-1][0])+abs(df.y-center_B[-1][1])
    
def euclidean():
    df['distance_a']=np.sqrt((df.x-center_A[-1][0])**2+(df.y-center_A[-1][1])**2)
    df['distance_b']=np.sqrt((df.x-center_B[-1][0])**2+(df.y-center_B[-1][1])**2)
    
def trigonometric():
    df['distance_a']=abs(np.sin(np.sqrt((df.x-center_A[-1][0])**2+(df.y-center_A[-1][1])**2)))
    df['distance_b']=abs(np.cos(np.sqrt((df.x-center_B[-1][0])**2+(df.y-center_B[-1][1])**2)))
    

#generating the X and Y coordinates for the two circles
inner=np.random.ranf(1000)*np.pi*2
inner_y=np.sin(inner)*np.pi+0.1*np.random.ranf(1000)
inner_x=np.cos(inner)*np.pi+0.1*np.random.ranf(1000)
outer=np.random.ranf(1000)*np.pi*2
outer_y=np.sin(outer)*np.pi/2+(0.1*np.random.ranf(1000))
outer_x=np.cos(outer)*np.pi/2+(0.1*np.random.ranf(1000))
x=np.append(inner_x, outer_x)
y=np.append(inner_y, outer_y)
df=pd.DataFrame({'x':x, 'y':y})

#creating 2 random points in the space 
range_xy=(max(x)-min(x),max(y)-min(y))
two_points=np.random.rand(2,2)
tp=range_xy*two_points
center_A=[[min(x)+tp[0,0],min(y)+tp[0,1]]]
center_B=[[min(x)+tp[1,0],min(y)+tp[1,1]]]

#define a function that assigned each point to its nearest center
def assignment():
    assign=[]
    for i in range(0,df.shape[0]):
        if (df.distance_a[i]<df.distance_b[i]):
            assign+=['a']
        else:
            assign+=['b']
    df['assignment']=assign



'''specify the distance used'''
def distance():
    #trigonometric()
    manhattan()
    #euclidean()

#first assignment and first formation of the clusters
distance()
assignment()
da = df[df.assignment=='a']
db = df[df.assignment=='b']

#adding the new coordinates for the two centers:
center_A += [[da.x.mean(),da.y.mean()]]
center_B += [[db.x.mean(),db.y.mean()]]

#repeating the two precedent steps until convergence
while center_A[-1]!=center_A[-2]:
    distance()
    assignment()
    da = df[df.assignment=='a']
    db = df[df.assignment=='b']
    center_A += [[da.x.mean(),da.y.mean()]]
    center_B += [[db.x.mean(),db.y.mean()]]
    
#plotting the result
plt.scatter(da.x,da.y, marker='.')
plt.scatter(db.x,db.y, marker='.')
plt.scatter(center_A[-1][0],center_A[-1][1])
plt.scatter(center_B[-1][0],center_B[-1][1])