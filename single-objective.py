import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


def main():
    folder_path = 'ACI_Project2_2324_Data'
    file_list = os.listdir(folder_path)
    for file_name in file_list:
        if file_name.endswith('.csv'):
            # Extract the base name of the file (without the extension)
            df_name = os.path.splitext(file_name)[0]
            # Construct the full file path
            file_path = os.path.join(folder_path, file_name)
            
            # Read the CSV file into a DataFrame with the base name as the variable name
            globals()[df_name] = pd.read_csv(file_path)

if __name__ == "__main__":
    main()