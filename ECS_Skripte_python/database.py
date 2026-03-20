import sqlite3
import pandas as pd
import os

aktueller_ordner = os.path.dirname(__file__)
projekt_ordner = os.path.dirname(aktueller_ordner)
datenbank_pfad = os.path.join(projekt_ordner, 'Datenanalyse', 'ECS_Datenbank.db')

os.makedirs(os.path.dirname(datenbank_pfad), exist_ok=True)
print(f"Datenbank wird erstellt in: {datenbank_pfad}")

datenbank = sqlite3.connect(datenbank_pfad)