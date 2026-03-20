import pandas as pd
import glob
import os

ordner = "ECS_HHID"
ordner_pfad = os.listdir(ordner)

subOrdnerList = []
for subOrdner in ordner_pfad:
    pfad = os.path.join(ordner, subOrdner)
    if os.path.isdir(pfad):
        subOrdnerList.append(pfad)

for sub in subOrdnerList:

    # Alle CSV-Dateien im Ordner finden
    csv_dateien = glob.glob(os.path.join(sub, "*.csv"))

    # Basis erstellen
    df = pd.read_csv(csv_dateien[0], header = None, skiprows=17, encoding='latin-1')

    
    # HHID wird gelesen
    dfHH = pd.read_csv(csv_dateien[0], skiprows=1, header=None, nrows=10, encoding='latin-1')
    zeile = dfHH.iloc[2]
    hhid = zeile[1]

    for datei in csv_dateien[1:]:
        temp = pd.read_csv(datei, header = None, skiprows=17, encoding='latin-1')
        merged = pd.merge(df, temp, on=0, how='inner')
        merged.to_csv(os.path.join(sub, f"{hhid}_merged.csv"), index=False, header=False, encoding='latin-1')

