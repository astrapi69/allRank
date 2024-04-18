import pandas as pd

# Load the CSV file to inspect its structure
file_path = 'C:/Users/aster/dev/git/hub/astrapi69/allRank/allrank/transform/subset_exploded_df_merged_amenities.csv'
data = pd.read_csv(file_path, sep='\t')

# Safe checking of column existence and dynamic selection of feature columns

# Find all columns that could be considered as features (we assume they end with certain keywords if amenities are not directly named)
potential_feature_keywords = ['Internet', 'Tub', 'Laundry', 'Parking', 'Pets', 'Pool', 'Spa', 'Swimming', 'Dryer', 'WiFi']
features_found = [col for col in data.columns if any(keyword in col for keyword in potential_feature_keywords)]
additional_features = ['point_of_sale', 'geo_location_country', 'is_mobile', 'adult_count', 'child_count']
features_to_use = additional_features + features_found

# Checking for a plausible label column (assuming a label might be 'clicked' if it exists)
label_column = 'clicked' if 'clicked' in data.columns else data.columns[-1]  # Use the last column as label if 'clicked' is absent

# Assuming we create a synthetic 'clicked' column for demonstration as label (binary based on adult_count)
if label_column != 'clicked':
    data['clicked'] = (data['adult_count'] > 1).astype(int)
    label_column = 'clicked'

# Normalizing the dataset
normalized_data = {
    "features": data[features_to_use].values.tolist(),
    "labels": data[label_column].values.tolist()
}

# Confirming selected feature and label columns
features_to_use, label_column, normalized_data["features"][:2], normalized_data["labels"][:2]

