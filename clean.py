import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")

del df["Star_name"] 
del df["Distance"] 
del df["Mass"] 
del df["Radius"] 
del df["Luminosity"] 

df.to_csv("main.csv")

print(df.shape)