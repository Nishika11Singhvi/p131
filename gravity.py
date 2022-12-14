import csv
import pandas as pd

df=pd.read_csv("main.csv")
radius=df["Radius"].tolist()
mass=df["Mass"].tolist()
gravity=[]

def convert(radius,mass):
    for i in range(0,len(radius)-1): 
        radius[i] = radius[i]*6.957e+8 
        mass[i] = mass[i]*1.989e+30

convert(radius,mass)

def gravity(radius,mass):
    G=6.674e-11
    for index in range(0,len(mass)): 
        g= (mass[index]*G)/((radius[index])**2) 
        gravity.append(g)


gravity(radius,mass)

df["Gravity"]=gravity



