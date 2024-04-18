import pandas as pd
import gzip
import shutil

def subset_csv_file(csv_file_input_path, csv_file_output_path, subset_length):
    with open(csv_file_input_path, 'r') as file:
        df = pd.read_csv(file, sep='\t')
    subset_df = df.iloc[:subset_length]
    subset_df.to_csv(csv_file_output_path, sep='\t', index=False)      

def write_to_gzipfile(tsv_filename, tsv_gz_filename):
    with open(tsv_filename, 'rb') as f_in:
        with gzip.open(tsv_gz_filename, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

def preview_file(file_path, num_lines=5):
    with open(file_path, 'r') as file:
        for _ in range(num_lines):
            print(file.readline())

def read_gzip_file(file_path) -> pd.DataFrame:
    """
    Read a .tsv.gz compressed dataset file into a pandas DataFrame.

    Parameters:
    file_path (str): The file path to the .tsv.gz file.

    Returns:
    pd.DataFrame: A DataFrame containing the data from the .tsv.gz file.
    """
    # Use gzip.open to read the gzipped file in binary mode ('rb'), then parse it with pandas
    with gzip.open(file_path, 'rb') as file:
        df = pd.read_csv(file, sep='\t')
    return df
        


input_csv_path = 'C:/Users/aster/dev/git/hub/astrapi69/allRank/allrank/data/exploded_df_merged_amenities.csv'
output_csv_path = 'C:/Users/aster/dev/git/hub/astrapi69/allRank/allrank/data/subset_exploded_df_merged_amenities.csv'

subset_csv_file(input_csv_path, output_csv_path, 5)

