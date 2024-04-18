import pandas as pd

def check_columns(input_file_path):
    # Load the dataset
    data = pd.read_csv(input_file_path, sep='\t')
    
    # Print all column names
    print("Columns in the CSV file:", data.columns.tolist())