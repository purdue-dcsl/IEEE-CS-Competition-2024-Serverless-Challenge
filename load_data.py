import os
import pandas as pd

def load_csv_files_from_folder(folder_path):
    csv_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path)]
    df_list = [pd.read_csv(file_path) for file_path in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)
    
    return combined_df

if __name__ == "__main__":
    training_folder = 'training'
    testing_folder = 'testing'
    
    training_df = load_csv_files_from_folder(training_folder)
    testing_df = load_csv_files_from_folder(testing_folder)
    