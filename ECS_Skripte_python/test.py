
import pandas as pd
import os
import shutil  

# This file is for testing purposes, to check if we can read the meta data and the data from the csv files correctly. It is not part of the final code, but it helps us to understand how to extract the information we need for our analysis.

ordner = "ECS_RAW"
ornder_pfad = os.path.dirname(ordner)

datei_pfad= os.path.join(ordner, 'EXACTv2 29262_2025-11-29_14-56-13_CLEAN.csv')
df = pd.read_csv(datei_pfad, skiprows=1, header=None, nrows=14, encoding='latin-1')

hhid = str(df.iloc[2, 1]).strip()
sensor_id = str(df.iloc[3, 1]).strip()
max_temp = str(df.iloc[8, 1]).strip()
name = str(df.iloc[10, 1]).strip()
cooking_days = str(df.iloc[13, 1]).strip()


print(hhid)
print(sensor_id)
print(max_temp)
print(name)
print(cooking_days)



            
    

