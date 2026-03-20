import pandas as pd
import os

ordner = "ECS_CLEAN"
auswertung = "ECS_HHID"
all_data = os.listdir(ordner)
auswertung_pfad = os.listdir(auswertung)

einzelne_datei = os.path.join(ordner, "FUELv2 25010_2025-11-27_12-26-49_CLEAN.csv")

df = pd.read_csv(einzelne_datei, skiprows=17, encoding='latin-1')

print(df.head())