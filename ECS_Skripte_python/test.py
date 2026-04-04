import pandas as pd
import os
import glob
import shutil

# This file is for testing purposes, to check if we can read the meta data and the data from the csv files correctly. It is not part of the final code, but it helps us to understand how to extract the information we need for our analysis.

current = os.path.dirname(__file__)
project = os.path.dirname(current)

ornder_pfad = os.path.join(project, "ECS_HHID")
subordner_pfad = os.path.join(ornder_pfad, "301")
folder_list = []
folder_list.append(subordner_pfad)


def remove_longtime(folders):
    for folder in folders:
        if not os.path.isdir(folder):
            print("no")
            continue

        csv_files = glob.glob(os.path.join(folder, "*.csv"))

        for file in csv_files:
            try:
                df = pd.read_csv(file, skiprows=17, header=None, encoding="latin-1", nrows = 5041)
                firstStamp = df.iloc[1:2]
                lastStamp = df.iloc[-1:]
                print(file)
                print("__start___")
                print(firstStamp)
                print ("_end__")
                print(lastStamp)
                print ("______")

            except Exception as e:
                print(f"No good at {file}: {e}")


remove_longtime(folder_list)
