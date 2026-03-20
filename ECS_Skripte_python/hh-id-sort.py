import pandas as pd
import os
import shutil  


ordner = "ECS_CLEAN"
auswertung = "ECS_HHID"
all_data = os.listdir(ordner)
auswertung_pfad = os.listdir(auswertung)


for datei in all_data:
    if datei.endswith(".csv"):

        dateipfad = os.path.join(ordner, datei)
        df = pd.read_csv(dateipfad, skiprows=1, header=None, nrows=10, encoding='latin-1')

        # HHID wird gelesen
        zeile = df.iloc[2] 
        hhid = zeile[1]

        # Ordner erstelen und Dateien kopieren
        newFolder= os.path.join(auswertung, hhid)
        os.makedirs(newFolder, exist_ok=True)

        # Datei zu neuem Pfad kopieren
        goal = os.path.join(newFolder, datei)

        shutil.copy(dateipfad, goal)


            
    

