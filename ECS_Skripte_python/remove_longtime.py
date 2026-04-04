import os
import glob
import pandas as pd
from datetime import datetime

current_folder = os.path.dirname(__file__)
project_folder = os.path.dirname(current_folder)

fuel_folder = os.path.join(project_folder, "ECS_FUEL", "**")
excat_folder = os.path.join(project_folder, "ECS_EXCAT", "**")

fuel_subfolders = glob.glob(fuel_folder, recursive = True)
excat_subfolders = glob.glob(excat_folder, recursive= True)

time_format = "%Y-%m-%d %H:%M:%S"

def remove_longtime(folders):
    for folder in folders:
        if not os.path.isdir(folder):
            continue

        csv_files = glob.glob(os.path.join(folder, "*.csv"))

        file_data = []        

        for file in csv_files:

            try:
                df = pd.read_csv(file, skiprows=1, header=None, nrows=13, encoding='latin-1')
                begin_stamp = df.iloc[5, 1]
                end_stamp = df.iloc[6, 1]

                dt_start = datetime.strptime(begin_stamp, time_format)
                dt_end = datetime.strptime(end_stamp, time_format)

                if(dt_end - dt_start >= ):
                    os.remove(file)
                    print()
            except Exception as e:
                print(f"No good at {file}: {e}")