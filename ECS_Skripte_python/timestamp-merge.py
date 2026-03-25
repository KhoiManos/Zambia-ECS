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

    # Alle CSV-Dateien im Ordner finden und merged nicht als Input
    csv_dateien = [f for f in glob.glob(os.path.join(sub, "*.csv")) if "_merged" not in f]

    # Basis erstellen
    df = pd.read_csv(csv_dateien[0], header = None, skiprows=17, encoding='latin-1')
    if df.empty: 
        continue
    
    # HHID wird gelesen
    dfHH = pd.read_csv(csv_dateien[0], skiprows=1, header=None, nrows=10, encoding='latin-1')
    zeile = dfHH.iloc[2]
    hhid = zeile[1]
    df[0] = df[0].astype(str).str.strip()  # Whitespace entfernen

     # Spalten eindeutig benennen
    dateiname = os.path.splitext(os.path.basename(csv_dateien[0]))[0]
    df.columns = [0] + [f"{dateiname}_{i}" for i in range(1, len(df.columns))]


    for datei in csv_dateien[1:]:

        
        try:
            temp = pd.read_csv(datei, header = None, skiprows=17, encoding='latin-1')
        except pd.errors.EmptyDataError:
            print(f"⚠️ Übersprungen: {os.path.basename(datei)}")
            continue
        
        temp[0] = temp[0].astype(str).str.strip()  # Whitespace entfernen

        # Auch temp-Spalten eindeutig benennen
        dateiname = os.path.splitext(os.path.basename(datei))[0]
        temp.columns = [0] + [f"{dateiname}_{i}" for i in range(1, len(temp.columns))]

        merged = pd.merge(df, temp, on=0, how='inner')
        if not merged.empty:
            merged.to_csv(os.path.join(sub, f"{hhid}_merged.csv"), index=False, header=False, encoding='latin-1')
            df = merged
