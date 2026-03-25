import sqlite3
import pandas as pd
import os

aktueller_ordner = os.path.dirname(__file__)
projekt_ordner = os.path.dirname(aktueller_ordner)
datenbank_pfad = os.path.join(projekt_ordner, 'Datenanalyse', 'ECS_Datenbank.db')
testCSV_pfad = os.path.join(projekt_ordner, 'ECS_FUEL', '1', 'FUELv2 13374_2025-11-22_11-05-25 (2)_CLEAN.csv')

os.makedirs(os.path.dirname(datenbank_pfad), exist_ok=True)
print(f"Datenbank wird erstellt in: {datenbank_pfad}")

datenbank = sqlite3.connect(datenbank_pfad)
df = pd.read_csv(testCSV_pfad, skiprows = 17)
df.to_sql('fuel_ecs_1', datenbank, if_exists='replace', index=False)

df_abfrage = pd.read_sql_query("SELECT * FROM fuel_ecs_1 WHERE \"Weight (kg)\" = 0.004487", datenbank)
print(df_abfrage)
datenbank.close()