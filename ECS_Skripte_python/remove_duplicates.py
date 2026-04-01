import duckdb
import os


sql_filepath = os.path.join("ECS_SQL", "transform.sql")
database_filepath = os.path.join("Datenanalyse", "ECS_Datenbank.db")

def run_duplicate_check(sql_path, db_path):
    if not os.path.exists(sql_path):
        print(f"❌ Fehler: SQL-Datei nicht gefunden unter {sql_path}")
        return

    con = duckdb.connect(db_path)
    
    try:
        with open(sql_path, 'r', encoding='utf-8') as f:
            full_sql = f.read()
        
        print(f"🚀 Starte Dubletten-Prüfung...")
        
        # Führt alle Schritte im SQL-File aus (Erstellt die TEMP TABLE)
        con.execute(full_sql)
        
        # Jetzt holen wir uns gezielt das Ergebnis aus der erstellten Tabelle
        # Wir fragen die Tabelle 'duplicates_to_remove' ab, die dein SQL erstellt hat
        df_duplicates = con.execute("SELECT * FROM duplicates_to_remove").df()
        
        if df_duplicates.empty:
            print("✅ Keine Dubletten gefunden.")
        else:
            print(f"⚠️ {len(df_duplicates)} Dubletten identifiziert:")
            print(df_duplicates[['file_to_remove', 'file_to_keep']])
            
            # Optional: Speicher die Liste der zu löschenden Pfade als Textdatei für später
            df_duplicates['file_to_remove'].to_csv("files_to_delete.txt", index=False, header=False)
            print("\n📄 Liste der Pfade wurde in 'files_to_delete.txt' gespeichert.")

    except Exception as e:
        print(f"💥 Fehler im SQL-Ablauf: {e}")
    finally:
        con.close()

run_duplicate_check(sql_filepath, database_filepath)