import json

import pandas as pd

from check_routines import *


def csv_to_allRank_jsonl_format(input_file_path, output_file_path, y_train_path):
     # Load the dataset
    data = pd.read_csv(input_file_path, sep='\t')
    
    
    # Print the first few rows to check the structure
    print("First few rows:", data.head())
    print("Data columns:", data.columns.tolist())

    # Define columns to drop
    features_to_drop = ['search_id', 'prop_id', 'booking_bool']  # Update or correct as necessary
    
    # Ensure only existing columns are dropped to avoid KeyError
    features_to_drop = [col for col in features_to_drop if col in data.columns]
    features = data.drop(columns=features_to_drop, errors='ignore')
    
    # Ensure the label column exists and is the last column if 'booking_bool' is missing
    label_col = 'is_trans' if 'is_trans' in data.columns else data.columns[-1]
    labels = pd.read_csv(y_train_path) # Do not convert yet

    # Check if labels can be converted to int (debugging step)
    try:
        labels_int = labels.astype(int)
    except ValueError as e:
        print(f"Error converting labels to int: {e}")
        print("Faulty labels:", labels[~labels.apply(lambda x: x.isdigit())])  # This assumes labels are expected to be digit strings

    # Proceed if no error (remove this line in actual use: return)

    # Writing to JSONLines format
    with open(output_file_path, 'w') as outfile:
        for index, row in features.iterrows():
            features_list = row.tolist()
            json_line = {"features": features_list, "labels": [int(labels[index])] if pd.notna(labels[index]) else [0]}
            json.dump(json_line, outfile)
            outfile.write('\n')


if __name__ == '__main__':    
    
    input_path = 'C:/Users/aster/dev/git/hub/astrapi69/allRank/allrank/data/X_train.csv'
    input_path = 'C:/Users/aster/dev/git/hub/astrapi69/allRank/allrank/data/X_train.csv'  # Update this path to your actual file path
    output_path = 'C:/Users/aster/dev/git/hub/astrapi69/allRank/allrank/data/output_data.jsonl'
    
    check_columns(input_path)
    
    # csv_to_allRank_jsonl_format(input_path, output_path)


"""     feature_cols = ['adult_count', 'geo_location_country', 'point_of_sale']  # example feature columns
    label_col = 'destination_id'  # this should be your target variable, e.g., clicks, purchases
    query_id_col = 'geo_location_country'

    X_train, y_train, qid_train = format_data_for_ranking(df, feature_cols, label_col, query_id_col)
    print("Train Features shape:", X_train.shape)
    print("Train Labels shape:", y_train.shape)
    print("Train Query IDs shape:", len(qid_train))
    X_val, y_val, qid_val = format_data_for_ranking(df, feature_cols, label_col, query_id_col)
    print("Validation Features shape:", X_val.shape)
    print("Validation Labels shape:", y_val.shape)
    print("Validation Query IDs shape:", len(qid_val))

    os.makedirs("dummy_data", exist_ok=True)
    dump_svmlight_file(X_train, y_train, os.path.join("dummy_data", "train.txt"), query_id=qid_train)
    dump_svmlight_file(X_val, y_val, os.path.join("dummy_data", "vali.txt"), query_id=qid_val) """
