import pandas as pd

# -----------------------------
# Load cleaned datasets
# -----------------------------
sas = pd.read_csv("./data/sas_cleaned_data.csv")
mohali = pd.read_csv("./data/mohali_cleaned_data.csv")
kharar = pd.read_csv("./data/kharar_cleaned_data.csv")

# -----------------------------
# Add city column
# -----------------------------
sas["city"] = "SAS Nagar"
mohali["city"] = "Mohali"
kharar["city"] = "Kharar"

# -----------------------------
# Merge datasets
# -----------------------------
merged_df = pd.concat(
    [sas, mohali, kharar],
    ignore_index=True
)

# -----------------------------
# Remove duplicates (if any)
# -----------------------------
merged_df.drop_duplicates(inplace=True)

# -----------------------------
# Basic Information
# -----------------------------
print("\nMerged Dataset Information")
print("-" * 40)
print(merged_df.info())

print("\nShape:", merged_df.shape)

print("\nMissing Values")
print("-" * 40)
print(merged_df.isnull().sum())

print("\nListings by City")
print("-" * 40)
print(merged_df["city"].value_counts())

print("\nSummary Statistics")
print("-" * 40)
print(merged_df.describe())

# -----------------------------
# Save merged dataset
# -----------------------------
merged_df.to_csv(
    "./data/punjab_rental_dataset.csv",
    index=False
)

print("\nPunjab Rental Dataset saved successfully!")